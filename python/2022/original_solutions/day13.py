# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 13

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
  # pp(plines)
  pass

### part 1


def compare(l1, l2):
  idx = 0
  while True:
    if len(l1) < idx + 1 and len(l2) >= idx + 1:
      return 1
    if len(l2) < idx + 1 and len(l1) >= idx + 1:
      return -1
    if len(l1) < idx + 1 and len(l2) < idx + 1:
      return 0

    a = l1[idx]
    b = l2[idx]

    if isinstance(a, list) and not isinstance(b, list):
      b = [b]

    if isinstance(b, list) and not isinstance(a, list):
      a = [a]

    if isinstance(a, list) and isinstance(b, list):
      v = compare(a, b)
    else:
      v = 1 if a < b else -1 if a > b else 0

    if v < 0:
      return -1
    if v > 0:
      return 1

    idx += 1

  return 1


right_pairs = []

for idx, i in enumerate(range(0, len(plines), 3), 1):
  l1 = eval(plines[i])
  l2 = eval(plines[i + 1])
  # pp((idx, l1, l2))

  c = compare(l1, l2)
  if c > 0:
    right_pairs.append(idx)

ans = sum(right_pairs)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

plines = [eval(line) for line in plines if line] + [[[2]], [[6]]]
# pp(plines)

import functools

plines.sort(key=functools.cmp_to_key(compare), reverse=True)
# pp(plines)

indexes = []
for i, line in enumerate(plines, 1):
  if line == [[2]]:
    indexes.append(i)
  if line == [[6]]:
    indexes.append(i)

ans = indexes[0] * indexes[1]
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
