import networkx as nx

from utils import aoc
from utils.helpers import get_dgrid, graph_from_dgrid

YEAR, DAY = 2022, 12

fin = aoc.get_input(DAY)
heightmap = get_dgrid(fin, cast=lambda c: 0 if c == 'S' else 27 if c == 'E' else ord(c) - ord('a') + 1)

source = None
target = None
start_elevations = []
for pos, height in heightmap.items():
  if height == 0:
    source = pos
    heightmap[pos] = 1
  elif height == 27:
    target = pos
    heightmap[pos] = 26

  if heightmap[pos] == 1:
    start_elevations.append(pos)

g = graph_from_dgrid(
  heightmap,
  weighted=False,
  edge_filter=lambda s, t, sw, tw: tw - sw <= 1,
  use_nx_digraph=True,
)

ans = nx.shortest_path_length(g, source=source, target=target)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

paths = set()
for start in start_elevations:
  try:
    paths.add(nx.shortest_path_length(g, source=start, target=target))
  except Exception:
    pass

ans = min(paths)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
