# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2016, 2

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t.strip() for t in line.split(',')]

  pattern = '{}-{}\n'
  # tokens = parse.search(parse_pattern, line).fixed

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
    plines = [parse_line(line) for line in lines][0]
    #plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

# pp(plines)

### part 1

ans = 0

c = (0, 0)
d = (0, 1)

locs = {c}
first_loc_twice = None

for p in plines:
  v = int(p[1:])
  if p[0] == 'R':
    if d == (0, 1):
      d = (1, 0)
    elif d == (1, 0):
      d = (0, -1)
    elif d == (0, -1):
      d = (-1, 0)
    else:
      d = (0, 1)
  else:
    if d == (0, 1):
      d = (-1, 0)
    elif d == (1, 0):
      d = (0, 1)
    elif d == (0, -1):
      d = (1, 0)
    else:
      d = (0, -1)
  for _ in range(v):
    c = element_sum(c, d)
    if c in locs and first_loc_twice is None:
      first_loc_twice = c
    locs.add(c)

ans = manhattan_dis(c, (0, 0))

aoc.print_answer(ans, 1)
if not DEBUG:
  yn = input("Submit part 1 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

ans = manhattan_dis(first_loc_twice, (0, 0))

aoc.print_answer(ans, 2)
if not DEBUG:
  yn = input("Submit part 2 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 2, DAY, YEAR)
