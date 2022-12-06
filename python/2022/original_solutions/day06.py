# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 6

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
l = deque()

t = 0
for i, c in enumerate(line):
  if len(l) == 4:
    l.popleft()
  l.append(c)
  if len(set(l)) == 4:
    t = i + 1
    break

ans = t
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

s = set()
d = {}
l = deque()

t = 0
for i, c in enumerate(line):
  if len(l) == 14:
    l.popleft()
  l.append(c)
  if len(set(l)) == 14:
    t = i + 1
    break

ans = t
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
