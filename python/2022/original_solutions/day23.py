# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 23

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  return line

  tokens = [t for t in line.split(' ')]
  return tokens

  pattern = '{} {:d}'
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

elves = {k for k, v in dg.items() if v == '#'}
bak_elves = elves.copy()

dirs = [
  (
    ((0, -1), (1, -1), (-1, -1)),
    (0, -1),
  ),
  (
    ((0, 1), (1, 1), (-1, 1)),
    (0, 1),
  ),
  (
    ((-1, 0), (-1, -1), (-1, 1)),
    (-1, 0),
  ),
  (
    ((1, 0), (1, -1), (1, 1)),
    (1, 0),
  ),
]

ROUNDS = 10
for r in range(ROUNDS):
  # print_dgrid(dg)

  not_move = set()

  proposed = defaultdict(list)
  for e in elves:
    x = True
    for neighbor in dgrid_neighbors8_values(dg, e, default='.'):
      if neighbor != '.':
        x = False
        break
    if x:
      continue

    for ds, target in dirs:
      used = False
      for d in ds:
        c = element_sum(e, d)
        if dg.get(c, '.') != '.':
          used = True
          break
      if not used:
        proposed[element_sum(e, target)].append(e)
        break

  # if r == 2:
  #   pp(proposed)

  for target_pos, es in proposed.items():
    if len(es) != 1:
      continue
    e = es[0]
    elves.remove(e)
    elves.add(target_pos)
    dg[e] = '.'
    dg[target_pos] = '#'

  dirs = dirs[1:] + [dirs[0]]

# print_dgrid(dg)

minx = min(x for x, y in elves)
maxx = max(x for x, y in elves)
miny = min(y for x, y in elves)
maxy = max(y for x, y in elves)

# pp((minx, maxx, miny, maxy, len(elves)))

ans = (maxx - minx + 1) * (maxy - miny + 1) - len(elves)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

elves = bak_elves.copy()
dg = {e: '#' for e in elves}

dirs = [
  (
    ((0, -1), (1, -1), (-1, -1)),
    (0, -1),
  ),
  (
    ((0, 1), (1, 1), (-1, 1)),
    (0, 1),
  ),
  (
    ((-1, 0), (-1, -1), (-1, 1)),
    (-1, 0),
  ),
  (
    ((1, 0), (1, -1), (1, 1)),
    (1, 0),
  ),
]

r = 1
while True:
  proposed = defaultdict(list)
  for e in elves:
    x = True
    for neighbor in dgrid_neighbors8_values(dg, e, default='.'):
      if neighbor != '.':
        x = False
        break
    if x:
      continue

    for ds, target in dirs:
      used = False
      for d in ds:
        c = element_sum(e, d)
        if dg.get(c, '.') != '.':
          used = True
          break
      if not used:
        proposed[element_sum(e, target)].append(e)
        break

  if not proposed:
    break

  for target_pos, es in proposed.items():
    if len(es) != 1:
      continue
    e = es[0]
    elves.remove(e)
    elves.add(target_pos)
    dg[e] = '.'
    dg[target_pos] = '#'

  dirs = dirs[1:] + [dirs[0]]

  r += 1

ans = r
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
