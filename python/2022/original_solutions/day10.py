# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 10

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
  (minx, miny), (maxx, maxy) = dgrid_coord_ranges(dg)
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
l = []

r = 1
cycles = 0
inst = 0
running = 0
to_add = 0

signals = []

while True:
  if inst >= len(plines):
    break

  line = plines[inst]
  tokens = line.split(' ')
  cmd = tokens[0]

  if running:
    running -= 1
    cycles += 1

    # pp((cycles, r))
    if cycles in (20, 60, 100, 140, 180, 220):
      # if cycles in (2, 6, 10, 14, 18, 22):
      # pp((cycles, r))
      s = r * cycles
      signals.append(s)
      if cycles == 220:
        break

    if not running:
      r += to_add
      to_add = 0

    continue

  if cmd == 'noop':
    running = 1
    to_add = 0
  elif cmd == 'addx':
    val = int(tokens[1])
    running = 2
    to_add = val

  inst += 1

# pp(signals)

ans = sum(signals)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

dg = {}

x = 0
y = 0

r = 1
cycles = 0
inst = 0
running = 0
to_add = 0

signals = []

while True:
  if inst >= len(plines):
    break

  line = plines[inst]
  tokens = line.split(' ')
  cmd = tokens[0]

  if running:
    running -= 1
    cycles += 1

    # pp((cycles, r))
    if x in (r - 1, r, r + 1):
      dg[(x, y)] = '#'
    else:
      dg[(x, y)] = '.'
    # print_dgrid(dg)

    x += 1
    if x > 39:
      x = 0
      y += 1

    if not running:
      r += to_add
      to_add = 0

    continue

  if cmd == 'noop':
    running = 1
    to_add = 0
  elif cmd == 'addx':
    val = int(tokens[1])
    running = 2
    to_add = val

  inst += 1

print_dgrid(dg)

ans = "EHPZPJGL"
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
