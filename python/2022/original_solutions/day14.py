# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 14

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

dg = {}

for i, line in enumerate(plines):
  tokens = [tuple(int(y) for y in x.split(',')) for x in line.split(' -> ')]

  x, y = tokens[0]

  for x2, y2 in tokens[1:]:
    dg[(x, y)] = '#'
    dg[(x2, y2)] = '#'
    while (x, y) != (x2, y2):
      if x < x2:
        x += 1
      elif x > x2:
        x -= 1
      elif y < y2:
        y += 1
      elif y > y2:
        y -= 1
      dg[(x, y)] = '#'

abyss_y = -math.inf
for k, v in dg.items():
  _, y = k
  abyss_y = max(abyss_y, y)


def next_sand(s):
  next_s = element_sum(s, (0, 1))
  if dg.get(next_s, '.') == '.':
    return next_s, True
  next_s = element_sum(s, (-1, 1))
  if dg.get(next_s, '.') == '.':
    return next_s, True
  next_s = element_sum(s, (1, 1))
  if dg.get(next_s, '.') == '.':
    return next_s, True
  return s, False


sand = (500, 0)
units = 0

i = 0
while True:
  prev_sand = sand
  sand, moved = next_sand(sand)

  if sand[1] >= abyss_y:
    break

  if moved:
    dg[prev_sand] = '.'
    dg[sand] = '+'
  else:
    dg[sand] = 'o'
    units += 1
    sand = (500, 0)

  i += 1
  # print_dgrid(dg)
  # if i == 10:
  #   break

ans = units
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

dg = {}

for i, line in enumerate(plines):
  tokens = [tuple(int(y) for y in x.split(',')) for x in line.split(' -> ')]

  x, y = tokens[0]

  for x2, y2 in tokens[1:]:
    dg[(x, y)] = '#'
    dg[(x2, y2)] = '#'
    while (x, y) != (x2, y2):
      if x < x2:
        x += 1
      elif x > x2:
        x -= 1
      elif y < y2:
        y += 1
      elif y > y2:
        y -= 1
      dg[(x, y)] = '#'

abyss_y = -math.inf
for k, v in dg.items():
  _, y = k
  abyss_y = max(abyss_y, y)
floor = abyss_y + 2


def next_sand(s):
  x, y = s

  if y + 1 == floor:
    return s, False

  next_s = element_sum(s, (0, 1))
  if dg.get(next_s, '.') == '.':
    return next_s, True
  next_s = element_sum(s, (-1, 1))
  if dg.get(next_s, '.') == '.':
    return next_s, True
  next_s = element_sum(s, (1, 1))
  if dg.get(next_s, '.') == '.':
    return next_s, True
  return s, False


sand = (500, 0)
units = 0

i = 0
while True:
  prev_sand = sand
  sand, moved = next_sand(sand)

  if moved:
    dg[prev_sand] = '.'
    dg[sand] = '+'
  else:
    dg[sand] = 'o'
    units += 1
    if sand == (500, 0):
      break
    sand = (500, 0)

  i += 1
  # print_dgrid(dg)
  # if units == 93:
  #   break

ans = units
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
