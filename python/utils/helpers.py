import re
from collections import defaultdict

from .algorithms import dgrid_neighbors4

MAX_CACHE_SIZE = 4 * 2**20  # int = 4bytes -> 4GB


def get_ints(f):
  return list(map(int, f.readlines()))


def get_lines(f, regex=None, parse_pattern=None, strip=True, re_cast=None):
  if parse_pattern is not None:
    import parse
    return [parse.search(parse_pattern, line.strip() if strip else line).fixed for line in f.readlines()]
  if regex is not None:
    if re_cast is None:
      return [re.compile(regex).findall(line.strip() if strip else line)[0] for line in f.readlines()]
    return [[re_cast(v) for v in re.compile(regex).findall(line.strip() if strip else line)[0]]
            for line in f.readlines()]

  return [line.strip() if strip else line for line in f.readlines()]


def get_dgrid(f, cast=None, start=(0, 0), y_start_at_top=True, strip=True):
  start_x, start_y = start
  dg = {}

  lines = f.readlines()
  if not y_start_at_top:
    lines = lines[::-1]

  for i, line in enumerate(lines):
    if strip:
      line = line.rstrip()
    y = start_y + i
    for j, c in enumerate(line):
      x = start_x + j
      dg[(x, y)] = c if cast is None else cast(c)

  return dg


def graph_from_dgrid(
  dg,
  weighted=True,
  neighbors=dgrid_neighbors4,
  weight_calc=lambda sw, tw: tw,
  edge_filter=lambda s, t, sw, tw: True,
  use_nx_digraph=False,
):
  g = defaultdict(list)
  for pos in dg:
    for adj in neighbors(dg, pos, only_existing=True):
      if not edge_filter(pos, adj, dg[pos], dg[adj]):
        continue
      if weighted:
        g[pos].append((adj, weight_calc(dg[pos], dg[adj])))
      else:
        g[pos].append(adj)
  if use_nx_digraph:
    return graph_to_nx_digraph(g, weighted=weighted)
  return g


def graph_to_nx_digraph(g, weighted=True):
  import networkx as nx

  di_graph = nx.DiGraph()
  for start, end_nodes in g.items():
    for end in end_nodes:
      if weighted:
        end_node, weight = end
        di_graph.add_edge(start, end_node, weight=weight)
      else:
        di_graph.add_edge(start, end)
  return di_graph


def print_dgrid(dg, default_val='.', mapping=None, y_start_at_top=True, add_end_break=True):
  if not dg:
    return

  min_x = int(min(dg.keys(), key=lambda p: p[0])[0])
  max_x = int(max(dg.keys(), key=lambda p: p[0])[0])
  min_y = int(min(dg.keys(), key=lambda p: p[1])[1])
  max_y = int(max(dg.keys(), key=lambda p: p[1])[1])

  yrange_step = ((min_y, max_y + 1, 1) if y_start_at_top else (max_y, min_y - 1, -1))
  for y in range(*yrange_step):
    line = ''
    for x in range(min_x, max_x + 1):
      val = dg.get((x, y), default_val)
      line += str(mapping.get(val, val) if mapping is not None else val)
    print(line)  # noqa: T201
  if add_end_break:
    print()  # noqa: T201
