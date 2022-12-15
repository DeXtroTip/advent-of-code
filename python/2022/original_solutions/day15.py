# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 15

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  # return line

  # tokens = [t for t in line.split(' ')]
  # return tokens

  pattern = 'Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}'
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

s = set()
d = {}
l = []

dg = {}

TARGET = 10 if DEBUG else 2000000

sb = {}

for sx, sy, bx, by in plines:
  dg[(sx, sy)] = 'S'
  dg[(bx, by)] = 'B'
  sb[(sx, sy)] = (bx, by)

# print_dgrid(dg)

dg_ranges = defaultdict(lambda: '.')

target_used = set()

for sensor, beacon in sb.items():
  x, y = sensor

  dis = manhattan_dis(sensor, beacon)
  minx = x - dis
  maxx = x + dis
  miny = y - dis
  maxy = y + dis

  if miny >= TARGET or TARGET >= maxy:
    continue

  g = dis - abs(TARGET - y)
  sg1 = x - g
  sg2 = x + g
  # pp((sensor, beacon, g, sg1, sg2, abs(TARGET - y)))

  for xx in range(sg1, sg2 + 1):
    target_used.add(xx)

# pp(dgrid_coord_ranges(dg_ranges))

# for sensor, beacon in sb.items():
#   dg_ranges[sensor] = 'S'
#   dg_ranges[beacon] = 'B'

# print_dgrid(dg_ranges)

ans = len(target_used) - 1
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

search_range = (0, 20) if DEBUG else (0, 4000000)
smin, smax = search_range

from z3 import *

x = Int('x')
y = Int('y')
s = Solver()
s.add(x >= smin, x <= smax, y >= smin, y <= smax)

for sensor, beacon in sb.items():
  dis = manhattan_dis(sensor, beacon)
  sx, sy = sensor
  s.add(
    Or(
      dis < ((x - sx) + (y - sy)),
      dis < ((sx - x) + (y - sy)),
      dis < ((x - sx) + (sy - y)),
      dis < ((sx - x) + (sy - y)),
    ))

s.check()
m = s.model()
fx = m[x].as_long()
fy = m[y].as_long()

ans = fx * 4000000 + fy
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
