# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 18

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  # return line

  # tokens = [t for t in line.split(' ')]
  # return tokens

  pattern = '{:d},{:d},{:d}'
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

cubes = set(plines)


def get_adjacent(c):
  x, y, z = c
  return (
    (x - 1, y, z),
    (x + 1, y, z),
    (x, y - 1, z),
    (x, y + 1, z),
    (x, y, z - 1),
    (x, y, z + 1),
  )


def solve(cubes):
  exposed = 0

  for c in cubes:
    for a in get_adjacent(c):
      if a not in cubes:
        exposed += 1

  return exposed


ans = solve(cubes)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

minx = math.inf
maxx = -math.inf
miny = math.inf
maxy = -math.inf
minz = math.inf
maxz = -math.inf

for c in cubes:
  x, y, z = c
  minx = min(minx, x)
  maxx = max(maxx, x)
  miny = min(miny, y)
  maxy = max(maxy, y)
  minz = min(minz, z)
  maxz = max(maxz, z)


def is_on_limit(c):
  x, y, z = c
  return x <= minx or x >= maxx or y <= miny or y >= maxy or z <= minz or z >= maxz


def is_inside(cubes, c):
  if is_on_limit(c):
    return False

  queue = deque((c, ))
  seen = {c}
  while queue:
    c = queue.popleft()
    for adjacent in get_adjacent(c):
      if adjacent in seen:
        continue
      seen.add(adjacent)
      if adjacent in cubes:
        continue
      if is_on_limit(adjacent):
        return False
      queue.append(adjacent)
  return True


cubes_inside = set()

for x in range(minx, maxx + 1):
  for y in range(miny, maxy + 1):
    for z in range(minz, maxz + 1):
      c = (x, y, z)
      if is_inside(cubes, c):
        cubes_inside.add(c)

all_cubes = cubes | cubes_inside

ans = solve(all_cubes)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
