# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 8

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
  dg = get_dgrid(fin, cast=int, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

if DEBUG:
  # print_dgrid(dg)
  # pp(plines)
  pass

### part 1

s = set()
d = {}
l = []

visible = 0
trees = set()

for pos, h in dg.items():
  ar = list(dgrid_neighbors4_values(dg, pos, default=-1))
  if -1 in ar:
    trees.add(pos)
    visible += 1
    continue
  failed = False
  found = False
  x, y = pos

  failed = False
  for ix in range(0, len(line)):
    # pp((pos, h, (ix, y), dg[(ix, y)]))
    if ix == x:
      if not failed:
        visible += 1
        found = True
      break
    if dg[(ix, y)] >= h:
      failed = True
      break
  if found:
    trees.add(pos)
    continue
  if not failed:
    trees.add(pos)
    visible += 1
    continue

  failed = False
  for ix in range(x + 1, len(line)):
    # pp((pos, h, (ix, y), dg[(ix, y)]))
    if ix == x:
      if not failed:
        visible += 1
        found = True
      break
    if dg[(ix, y)] >= h:
      failed = True
      break
  if found:
    trees.add(pos)
    continue
  if not failed:
    trees.add(pos)
    visible += 1
    continue

  failed = False
  for iy in range(0, len(line)):
    # pp((pos, h, (x, iy), dg[(x, iy)]))
    if iy == y:
      if not failed:
        visible += 1
        found = True
      break
    if dg[(x, iy)] >= h:
      failed = True
      break
  if found:
    trees.add(pos)
    continue
  if not failed:
    trees.add(pos)
    visible += 1
    continue

  failed = False
  for iy in range(y + 1, len(line)):
    # pp((pos, h, (x, iy), dg[(x, iy)]))
    if iy == y:
      if not failed:
        visible += 1
        found = True
      break
    if dg[(x, iy)] >= h:
      failed = True
      break
  if found:
    trees.add(pos)
    continue
  if not failed:
    trees.add(pos)
    visible += 1
    continue

ans = visible
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

f = set()

for x, y in trees:
  # if (x, y) != (0, 0):
  #   continue

  v = dg[(x, y)]
  # print((x, y, v))

  t = 1

  ct = 0
  for i, ix in enumerate(range(x - 1, -1, -1), 1):
    ct += 1
    nv = dg[(ix, y)]
    # pp((ix, y, nv))
    if nv >= v:
      break
  if ct != 0:
    t *= ct

  ct = 0
  for i, ix in enumerate(range(x + 1, len(line)), 1):
    ct += 1
    nv = dg[(ix, y)]
    # pp((ix, y, nv))
    if nv >= v:
      break
  if ct != 0:
    t *= ct

  ct = 0
  for i, iy in enumerate(range(y - 1, -1, -1), 1):
    ct += 1
    nv = dg[(x, iy)]
    if nv >= v:
      break
  if ct != 0:
    t *= ct

  ct = 0
  for i, iy in enumerate(range(y + 1, len(line)), 1):
    ct += 1
    nv = dg[(x, iy)]
    if nv >= v:
      break
  if ct != 0:
    t *= ct

  f.add(t)

ans = max(f)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
