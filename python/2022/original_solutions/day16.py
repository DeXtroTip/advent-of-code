# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 16

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  return line

  tokens = [t for t in line.split(' ')]
  return tokens

  pattern = 'Valve {} has flow rate={:d}; tunnel leads to valve{}'
  tokens = parse.search(pattern, line).fixed

  return tokens


try:
  fin = aoc.get_input(DAY, example=DEBUG)
  ints = get_ints(fin)
except:
  pass

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  lines = get_lines(fin, strip=True, parse_pattern=None)
except:
  lines = None
finally:
  if lines is not None:
    plines = [parse_line(line) for line in lines]
    # plines = [int(n) for n in plines]
    line = plines[0] if plines else None

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  is_weighted = True
  g = graph_from_dgrid(
    dg,
    weighted=is_weighted,
    neighbors=dgrid_neighbors4,
    weight_calc=lambda sw, tw: tw,
    edge_filter=lambda s, t, sw, tw: True,
  )
  G = graph_to_nx_digraph(g, weighted=is_weighted)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

if DEBUG:
  # print_dgrid(dg)
  # pp(plines)
  pass

### part 1

d = {}

flows = {}

G = nx.DiGraph()

for i, line in enumerate(plines):
  tokens = line.split(' ')
  source = tokens[1]
  flow = int(tokens[4].split('=')[1][:-1])
  valves = [t.strip() for t in line.split('valve')[-1].split(',')]
  if valves[0].startswith('s'):
    valves[0] = valves[0][1:].strip()

  flows[source] = flow

  d[source] = valves
  for valve in valves:
    G.add_edge(source, valve)

###

MAX_MINUTES = 30


def solve(g, flows, start):
  track = {}
  totals = set()
  queue = deque(((start, 0, 0, 0, set(), set(), (start, )), ))
  seen = {start}
  while queue:
    curr_node, curr_pressure, total_pressure, minutes, activated, since_last, path = queue.popleft()
    flow = flows[curr_node]
    since_last.add(curr_node)

    minutes += 1

    # if len(path) > 3 and minutes == 5 and path[1] == 'DD' and path[2] == 'CC' and path[3] == 'BB':
    #   pp((curr_node, curr_pressure, total_pressure, minutes, activated, since_last, path))

    totals.add((total_pressure, tuple(activated), path))
    if minutes == MAX_MINUTES:
      continue

    if flow > 0 and curr_node not in activated:
      new_pressure = total_pressure + ((MAX_MINUTES - (minutes)) * flow)
      # pp((curr_node, new_pressure))
      queue.append((curr_node, curr_pressure + flow, new_pressure, minutes, activated | {curr_node}, set(), path))

    for adjacent in g[curr_node]:
      if adjacent in since_last:
        continue

      t = track.get((adjacent, minutes), -1)
      if t >= total_pressure:
        continue
      track[(adjacent, minutes)] = total_pressure

      queue.append(
        (adjacent, curr_pressure, total_pressure, minutes, activated, since_last | {curr_node}, path + (adjacent, )))

  # pp(totals)

  return max(t for t, a, p in totals)


total_pressure = solve(d, flows, 'AA')
ans = total_pressure
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

MAX_MINUTES = 26


def solve(g, flows, start):
  track = {}
  totals = set()
  queue = deque((((start, start), 0, 0, set(), (set(), set()), ((start, ), (start, ))), ), )
  seen = {start}
  while queue:
    curr_node_2, total_pressure, minutes, activated, since_last_2, path_2 = queue.popleft()

    curr_node_a, curr_node_b = curr_node_2
    since_last_a, since_last_b = since_last_2
    path_a, path_b = path_2

    flow_a, flow_b = flows[curr_node_a], flows[curr_node_b]
    since_last_a.add(curr_node_a)
    since_last_b.add(curr_node_b)

    minutes += 1

    # if len(path_a) > 1 and len(path_b) > 1 and minutes == 2 \
    #     and path_a[1] == 'II' and path_b[1] == 'DD':
    #   pp((curr_node, total_pressure, minutes, activated, since_last, path))

    totals.add((total_pressure, tuple(activated), path_2))
    if minutes == MAX_MINUTES:
      continue

    # activate a first
    if flow_a > 0 and curr_node_a not in activated:
      new_pressure = total_pressure + ((MAX_MINUTES - (minutes)) * flow_a)
      new_activated = activated | {curr_node_a}

      if flow_b > 0 and curr_node_b not in new_activated:
        new_pressure_2 = new_pressure + ((MAX_MINUTES - (minutes)) * flow_b)
        curr_nodes = (curr_node_a, curr_node_b)
        since_last = (set(), set())
        paths = (path_a, path_b)
        queue.append((curr_nodes, new_pressure_2, minutes, new_activated | {curr_node_b}, since_last, paths))

      any_added = False
      for adjacent_b in g[curr_node_b]:
        if adjacent_b in since_last_b:
          continue

        t1 = track.get((curr_node_a, adjacent_b, minutes), -1)
        t2 = track.get((adjacent_b, curr_node_a, minutes), -1)
        t = max(t1, t2)
        if t >= new_pressure:
          continue
        track[(curr_node_a, adjacent_b, minutes)] = new_pressure

        curr_nodes = (curr_node_a, adjacent_b)
        since_last = (set(), since_last_b | {curr_node_b})
        paths = (path_a, path_b + (adjacent_b, ))
        queue.append((curr_nodes, new_pressure, minutes, new_activated, since_last, paths))
        any_added = True

      if not any_added:
        # t1 = track.get((curr_node_a, curr_node_b, minutes), -1)
        # t2 = track.get((curr_node_b, curr_node_a, minutes), -1)
        # t = max(t1, t2)
        # if t >= new_pressure:
        #   continue
        # track[(curr_node_a, curr_node_b, minutes)] = new_pressure
        curr_nodes = (curr_node_a, curr_node_b)
        since_last = (set(), since_last_b)
        paths = (path_a, path_b)
        queue.append((curr_nodes, new_pressure, minutes, new_activated, since_last, paths))

    # activate b first
    if flow_b > 0 and curr_node_b not in activated:
      new_pressure = total_pressure + ((MAX_MINUTES - (minutes)) * flow_b)
      new_activated = activated | {curr_node_b}

      if flow_a > 0 and curr_node_a not in new_activated:
        new_pressure_2 = new_pressure + ((MAX_MINUTES - (minutes)) * flow_a)
        curr_nodes = (curr_node_a, curr_node_b)
        since_last = (set(), set())
        paths = (path_a, path_b)
        queue.append((curr_nodes, new_pressure_2, minutes, new_activated | {curr_node_a}, since_last, paths))

      any_added = False
      for adjacent_a in g[curr_node_a]:
        if adjacent_a in since_last_a:
          continue

        t1 = track.get((curr_node_b, adjacent_a, minutes), -1)
        t2 = track.get((adjacent_a, curr_node_b, minutes), -1)
        t = max(t1, t2)
        if t >= new_pressure:
          continue
        track[(adjacent_a, curr_node_b, minutes)] = new_pressure

        curr_nodes = (adjacent_a, curr_node_b)
        since_last = (since_last_a | {curr_node_a}, set())
        paths = (path_a + (adjacent_a, ), path_b)
        queue.append((curr_nodes, new_pressure, minutes, new_activated, since_last, paths))
        any_added = True

      if not any_added:
        # t1 = track.get((curr_node_a, curr_node_b, minutes), -1)
        # t2 = track.get((curr_node_b, curr_node_a, minutes), -1)
        # t = max(t1, t2)
        # if t >= new_pressure:
        #   continue
        # track[(curr_node_a, curr_node_b, minutes)] = new_pressure
        curr_nodes = (curr_node_a, curr_node_b)
        since_last = (since_last_a, set())
        paths = (path_a, path_b)
        queue.append((curr_nodes, new_pressure, minutes, new_activated, since_last, paths))

    # activate none, start with a
    for adjacent_a in g[curr_node_a]:
      if adjacent_a in since_last_a:
        continue

      for adjacent_b in g[curr_node_b]:
        if adjacent_b in since_last_b:
          continue

        t1 = track.get((adjacent_a, adjacent_b, minutes), -1)
        t2 = track.get((adjacent_b, adjacent_a, minutes), -1)
        t = max(t1, t2)
        if t >= total_pressure:
          continue
        track[(adjacent_a, adjacent_b, minutes)] = total_pressure

        curr_nodes = (adjacent_a, adjacent_b)
        since_last = (since_last_a | {curr_node_a}, since_last_b | {curr_node_b})
        paths = (path_a + (adjacent_a, ), path_b + (adjacent_b, ))
        queue.append((curr_nodes, total_pressure, minutes, activated, since_last, paths))

    # activate none, start with b
    for adjacent_b in g[curr_node_b]:
      if adjacent_b in since_last_b:
        continue

      for adjacent_a in g[curr_node_a]:
        if adjacent_a in since_last_a:
          continue

        t1 = track.get((adjacent_a, adjacent_b, minutes), -1)
        t2 = track.get((adjacent_b, adjacent_a, minutes), -1)
        t = max(t1, t2)
        if t >= total_pressure:
          continue
        track[(adjacent_a, adjacent_b, minutes)] = total_pressure

        curr_nodes = (adjacent_a, adjacent_b)
        since_last = (since_last_a | {curr_node_a}, since_last_b | {curr_node_b})
        paths = (path_a + (adjacent_a, ), path_b + (adjacent_b, ))
        queue.append((curr_nodes, total_pressure, minutes, activated, since_last, paths))

  # pp(totals)

  return max(t for t, a, p in totals)


ans = solve(d, flows, 'AA')
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
