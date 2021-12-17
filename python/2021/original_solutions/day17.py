# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 17

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  # tokens = [t for t in line.split(',')]

  pattern = 'target area: x={}..{}, y={}..{}\n'
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

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

x1, x2, y1, y2 = [int(x) for x in plines[0]]


def f(vx, vy):
  maxy = 0
  px, py = 0, 0
  while px <= x2 and py >= y1:
    px, py = px + vx, py + vy
    vx, vy = max(0, vx - 1), vy - 1
    maxy = max(maxy, py)
    if x1 <= px <= x2 and y1 <= py <= y2:
      return maxy
  return None


maxy = 0
for x in range(x2 + 1):
  for y in range(y1, abs(y1)):
    ty = f(x, y)
    if ty is not None:
      maxy = max(maxy, ty)

ans = maxy
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

cc = 0
for x in range(x2 + 1):
  for y in range(y1, abs(y1)):
    ty = f(x, y)
    if ty is not None:
      cc += 1

ans = cc
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
