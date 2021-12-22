# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 22

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{} x={}..{},y={}..{},z={}..{}\n'
  tokens = parse.search(pattern, line).fixed

  return tokens


try:
  fin = aoc.get_input(DAY, example=DEBUG)
  ints = get_ints(fin)
except:
  pass

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  lines = get_lines(fin, strip=False, parse_pattern=None)
except:
  lines = None
finally:
  if lines is not None:
    plines = [parse_line(line) for line in lines]
    # plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  # g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

# pp(plines)

rlines = []
for line in plines:
  t, (x1, x2, y1, y2, z1, z2) = line[0], list(map(int, line[1:]))
  rlines.append((1 if t == 'on' else 0, x1, x2, y1, y2, z1, z2))
rlines = rlines[::-1]

### part 1

cc = 0
for x in range(-50, 50 + 1):
  for y in range(-50, 50 + 1):
    for z in range(-50, 50 + 1):
      for line in rlines:
        t, x1, x2, y1, y2, z1, z2 = line
        if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
          cc += t
          break

ans = cc
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2


def intersect_region(r1, r2):
  ax1, ax2, ay1, ay2, az1, az2 = r1
  bx1, bx2, by1, by2, bz1, bz2 = r2

  rx1 = max(ax1, bx1)
  rx2 = min(ax2, bx2)
  if rx2 < rx1:
    return None

  ry1 = max(ay1, by1)
  ry2 = min(ay2, by2)
  if ry2 < ry1:
    return None

  rz1 = max(az1, bz1)
  rz2 = min(az2, bz2)
  if rz2 < rz1:
    return None

  return rx1, rx2, ry1, ry2, rz1, rz2


ps = []

cc = 0
for line in rlines:
  t, x1, x2, y1, y2, z1, z2 = line
  if t == 0:
    ps.append(line)
    continue

  sc = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

  intersections = []
  for p in ps:
    tp, x1p, x2p, y1p, y2p, z1p, z2p = p
    r = intersect_region((x1, x2, y1, y2, z1, z2), (x1p, x2p, y1p, y2p, z1p, z2p))
    # print(line, p, r)
    if r is not None:
      sc -= (r[1] - r[0] + 1) * (r[3] - r[2] + 1) * (r[5] - r[4] + 1)
      intersections.append(r)
  ps.append(line)

  for s in range(2, len(ps) + 1):
    for comb in combinations(intersections, s):
      r = comb[0]
      for rc in comb[1:]:
        r = intersect_region(r, rc)
        if r is None:
          break
      if r is not None:
        if len(comb) % 2 == 0:
          sc += (r[1] - r[0] + 1) * (r[3] - r[2] + 1) * (r[5] - r[4] + 1)
        else:
          sc -= (r[1] - r[0] + 1) * (r[3] - r[2] + 1) * (r[5] - r[4] + 1)

  cc += sc

ans = cc
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
