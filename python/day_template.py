# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2000, 0

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

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

if DEBUG:
  # print_dgrid(dg)
  pp(plines)
  pass

### part 1

for line in plines:
  pass

ans = 0

aoc.print_answer(ans, 1)
if not DEBUG:
  yn = input("Submit part 1 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

for line in plines:
  pass

ans = 0

aoc.print_answer(ans, 2)
if not DEBUG:
  yn = input("Submit part 2 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 2, DAY, YEAR)
