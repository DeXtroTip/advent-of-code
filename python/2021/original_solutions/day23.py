# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 23

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

# print(dg)
print_dgrid(dg)

### part 1

# done by hand
a = [3, 4, 3, 8]
b = [3, 5, 5]
c = [4, 3, 5]
d = [5, 8]

ans = 1 * sum(a) + 10 * sum(b) + 100 * sum(c) + 1000 * sum(d)
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

# done by hand
a = [10, 11, 5, 5, 5, 8]
b = [9, 8, 9, 4, 5, 6, 5, 5]
c = [3, 4, 8, 9, 5, 5]
d = [7, 10, 10, 10]

ans = 1 * sum(a) + 10 * sum(b) + 100 * sum(c) + 1000 * sum(d)
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
