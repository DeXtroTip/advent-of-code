# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 19

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  # return tokens
  return line


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
    #plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

# pp(lines)
scanners = []
for line in lines:
  if not line:
    continue
  if 'scanner' in line:
    scanners.append([])
  else:
    cs = tuple(int(n) for n in line.split(','))
    scanners[-1].append(cs)

# print(scanners)

### part 1


def normalize_dgrid(dg, sx=10, sy=10):
  nd = {(x, y): None for x in range(sx + 1) for y in range(sy + 1)}

  min_x = int(min(dg.keys(), key=lambda p: p[0])[0])
  max_x = int(max(dg.keys(), key=lambda p: p[0])[0])
  min_y = int(min(dg.keys(), key=lambda p: p[1])[1])
  max_y = int(max(dg.keys(), key=lambda p: p[1])[1])

  xshift = -min_x
  yshift = -min_y

  for y in range(max_y, min_y - 1, -1):
    for x in range(min_x, max_x + 1):
      if dg.get((x, y)) is not None:
        nd[(x + xshift, y + yshift)] = dg[(x, y)]
  return nd


def orientations_gen2d():
  yield lambda p: (p[0], p[1])
  yield lambda p: (-p[0], p[1])
  yield lambda p: (p[0], -p[1])
  yield lambda p: (-p[0], -p[1])

  yield lambda p: (p[1], p[0])
  yield lambda p: (-p[1], p[0])
  yield lambda p: (p[1], -p[0])
  yield lambda p: (-p[1], -p[0])


def orientations_gen():
  yield lambda p: (p[0], p[1], p[2])
  yield lambda p: (-p[0], p[1], p[2])
  yield lambda p: (p[0], -p[1], p[2])
  yield lambda p: (p[0], p[1], -p[2])
  yield lambda p: (-p[0], -p[1], p[2])
  yield lambda p: (p[0], -p[1], -p[2])
  yield lambda p: (-p[0], p[1], -p[2])
  yield lambda p: (-p[0], -p[1], -p[2])

  yield lambda p: (p[0], p[2], p[1])
  yield lambda p: (-p[0], p[2], p[1])
  yield lambda p: (p[0], -p[2], p[1])
  yield lambda p: (p[0], p[2], -p[1])
  yield lambda p: (-p[0], -p[2], p[1])
  yield lambda p: (p[0], -p[2], -p[1])
  yield lambda p: (-p[0], p[2], -p[1])
  yield lambda p: (-p[0], -p[2], -p[1])

  yield lambda p: (p[2], p[0], p[1])
  yield lambda p: (-p[2], p[0], p[1])
  yield lambda p: (p[2], -p[0], p[1])
  yield lambda p: (p[2], p[0], -p[1])
  yield lambda p: (-p[2], -p[0], p[1])
  yield lambda p: (p[2], -p[0], -p[1])
  yield lambda p: (-p[2], p[0], -p[1])
  yield lambda p: (-p[2], -p[0], -p[1])

  yield lambda p: (p[2], p[1], p[0])
  yield lambda p: (-p[2], p[1], p[0])
  yield lambda p: (p[2], -p[1], p[0])
  yield lambda p: (p[2], p[1], -p[0])
  yield lambda p: (-p[2], -p[1], p[0])
  yield lambda p: (p[2], -p[1], -p[0])
  yield lambda p: (-p[2], p[1], -p[0])
  yield lambda p: (-p[2], -p[1], -p[0])

  yield lambda p: (p[1], p[2], p[0])
  yield lambda p: (-p[1], p[2], p[0])
  yield lambda p: (p[1], -p[2], p[0])
  yield lambda p: (p[1], p[2], -p[0])
  yield lambda p: (-p[1], -p[2], p[0])
  yield lambda p: (p[1], -p[2], -p[0])
  yield lambda p: (-p[1], p[2], -p[0])
  yield lambda p: (-p[1], -p[2], -p[0])

  yield lambda p: (p[1], p[0], p[2])
  yield lambda p: (-p[1], p[0], p[2])
  yield lambda p: (p[1], -p[0], p[2])
  yield lambda p: (p[1], p[0], -p[2])
  yield lambda p: (-p[1], -p[0], p[2])
  yield lambda p: (p[1], -p[0], -p[2])
  yield lambda p: (-p[1], p[0], -p[2])
  yield lambda p: (-p[1], -p[0], -p[2])


def points_dis(dg):
  dis = defaultdict(set)
  sortedd = sorted(dg)
  for p1 in sortedd:
    for p2 in sortedd:
      if p1 == p2:
        continue
      pdis = tuple(c2 - c1 for c1, c2 in zip(p1, p2))
      dis[p1].add(pdis)
  return dis


beacons = 0

ds = []
for i, s in enumerate(scanners):
  d = set()
  for p in s:
    d.add(p)
  ds.append(d)

beacons = ds[0]
# print_dgrid(beacons)
# print()

# pp(points_dis(beacons))

while True:
  beacons_size = len(beacons)
  for d in ds:
    bp_dis = points_dis(beacons)
    for oi, ori in enumerate(orientations_gen()):
      nd = {ori(p) for p in d}
      pdis = points_dis(nd)
      # pp(pdis)

      shift = None
      oflag = False
      for bp, bpd in bp_dis.items():
        for p, pd in pdis.items():
          o = 1 + len(bpd.intersection(pd))
          if o >= 12:
            oflag = True
            shift = tuple(c2 - c1 for c1, c2 in zip(p, bp))
            # print(bp, p)
            break
        if oflag:
          break

      if oflag:
        print(shift)
        # print(beacons)
        for p in nd:
          np = tuple(c2 + c1 for c1, c2 in zip(p, shift))
          beacons.add(np)
        # print(beacons)
        break
  if beacons_size == len(beacons):
    break

# print_dgrid(beacons)
# print()

ans = len(beacons)
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

shifts = set()

while True:
  beacons_size = len(beacons)
  for d in ds:
    bp_dis = points_dis(beacons)
    for oi, ori in enumerate(orientations_gen()):
      nd = {ori(p) for p in d}
      pdis = points_dis(nd)
      # pp(pdis)

      shift = None
      oflag = False
      for bp, bpd in bp_dis.items():
        for p, pd in pdis.items():
          o = 1 + len(bpd.intersection(pd))
          if o >= 12:
            oflag = True
            shift = tuple(c2 - c1 for c1, c2 in zip(p, bp))
            # print(bp, p)
            break
        if oflag:
          break

      if oflag:
        shifts.add(shift)
        print(shift)
        # print(beacons)
        for p in nd:
          np = tuple(c2 + c1 for c1, c2 in zip(p, shift))
          beacons.add(np)
        # print(beacons)
        break
  if beacons_size == len(beacons):
    break

md = -math.inf
for d1, d2 in product(shifts, shifts):
  if d1 == d2:
    continue
  md = max(md, sum(abs(c2 - c1) for c1, c2 in zip(d1, d2)))

ans = md
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
