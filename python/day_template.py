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
  pp(plines)
  pass

### part 1

s = set()
d = {}
l = []

for i, line in enumerate(plines):
  if not line:
    continue

  for j, col in enumerate(plines[i]):
    pass

  pass

ans = 0
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

s = set()
d = {}
l = []

for i, line in enumerate(plines):
  if not line:
    continue

  for j, col in enumerate(plines[i]):
    pass

  pass

ans = 0
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
