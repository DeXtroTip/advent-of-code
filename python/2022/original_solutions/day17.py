# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 17

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

rocks = [
  ["####"],
  [
    ".#.",
    "###",
    ".#.",
  ],
  [
    "..#",
    "..#",
    "###",
  ],
  [
    "#",
    "#",
    "#",
    "#",
  ],
  [
    "##",
    "##",
  ],
]

## part 1

count = 0

curr_rock = -1
rr = None

dg = {(x, -1): '-' for x in range(0, 8)}
highest = -1

import itertools

for i, jet in enumerate(itertools.cycle(line), 1):
  if count == 2022:
    break

  if rr is None:
    curr_rock = (curr_rock + 1) % len(rocks)
    rx, ry = 2, highest + 3

    rr = set()
    rock_type = rocks[curr_rock]
    move_up = len(rock_type)
    for rowy, row in enumerate(rock_type):
      for rowx, col in enumerate(row):
        if col == '#':
          rr.add((rx + rowx, ry - rowy + move_up))

    # pp((rx, ry, sorted(rr)))

  failed = False
  new_rr = set()
  if jet == '<':
    for x, y in rr:
      if x - 1 < 0 or dg.get((x - 1, y), '.') == '#':
        failed = True
        break
      new_rr.add((x - 1, y))
  else:
    for x, y in rr:
      if x + 1 > 6 or dg.get((x + 1, y), '.') == '#':

        failed = True
        break
      new_rr.add((x + 1, y))

  if failed:
    new_rr = rr

  # if count == 2:
  #   pp((i, jet, rr, new_rr))

  has_stop = False
  new_rr_2 = set()
  for x, y in new_rr:
    if dg.get((x, y - 1), '.') in ('#', '-'):
      has_stop = True
      break
    new_rr_2.add((x, y - 1))

  prev_rr = rr

  # if count == 2:
  #   pp((i, jet, prev_rr, new_rr_2 or new_rr))

  if has_stop:
    count += 1
    rr = None
    new_rr_2 = new_rr
    for x, y in new_rr_2:
      dg[(x, y)] = '#'
    highest = max(y for (x, y), v in dg.items() if v in ('-', '#'))
  else:
    rr = new_rr_2

  # if count == 2:
  #   print_dgrid(dg, y_start_at_top=False)

  # if i == 5:
  #   break

# print_dgrid(dg, y_start_at_top=False)

ans = highest + 1
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

GOAL = 1000000000000

# found manually -> found repeat pattern and selected the beggining lines that contain all 5 rock types
if DEBUG:
  repeated = [
    ".##....",
    ".##...#",
    "..#...#",
    "..#.###",
    "..#..#.",
    "..#.###",
    ".#####.",
  ]
else:
  repeated = [
    "..##...",
    "..##...",
    "...#...",
    "...#...",
    "...##..",
    "...##..",
    "..####.",
    "....###",
    ".....#.",
    "..####.",
  ]

repeated_first = None
repeated_second = None
repeated_diff = None
repeated_extra_counts = None
repeated_extra_values = None
repeated_goal = -1
repeated_extra_highest = None

count = 0

curr_rock = -1
rr = None

dg = {(x, -1): '-' for x in range(0, 7)}
highest = -1

import itertools

for i, jet in enumerate(itertools.cycle(line), 1):
  if count == repeated_goal:
    highest_diff = highest - repeated_extra_highest

    repeats = ((GOAL - repeated_first[0]) // repeated_diff[0]) - 1
    highest += repeats * repeated_diff[1]
    break

  if count == GOAL:
    break

  if rr is None:
    curr_rock = (curr_rock + 1) % len(rocks)
    rx, ry = 2, highest + 3

    rr = set()
    rock_type = rocks[curr_rock]
    move_up = len(rock_type)
    for rowy, row in enumerate(rock_type):
      for rowx, col in enumerate(row):
        if col == '#':
          rr.add((rx + rowx, ry - rowy + move_up))

    # pp((rx, ry, sorted(rr)))

  failed = False
  new_rr = set()
  if jet == '<':
    for x, y in rr:
      if x - 1 < 0 or dg.get((x - 1, y), '.') == '#':
        failed = True
        break
      new_rr.add((x - 1, y))
  else:
    for x, y in rr:
      if x + 1 > 6 or dg.get((x + 1, y), '.') == '#':

        failed = True
        break
      new_rr.add((x + 1, y))

  if failed:
    new_rr = rr

  has_stop = False
  new_rr_2 = set()
  for x, y in new_rr:
    if dg.get((x, y - 1), '.') in ('#', '-'):
      has_stop = True
      break
    new_rr_2.add((x, y - 1))

  if has_stop:
    count += 1
    rr = None
    new_rr_2 = new_rr
    for x, y in new_rr_2:
      dg[(x, y)] = '#'
    highest = max(y for (x, y), v in dg.items() if v in ('-', '#'))

    if highest >= len(repeated):
      block = []
      for y in range(highest, highest - len(repeated), -1):
        row = ""
        for x in range(0, 7):
          row += dg.get((x, y), '.')
        block.append(row)

      if block == repeated:
        if repeated_first is None:
          repeated_first = (count, highest)
        elif repeated_second is None:
          repeated_second = (count, highest)

          repeated_diff = (repeated_second[0] - repeated_first[0], repeated_second[1] - repeated_first[1])
          repeated_extra_counts = (GOAL - repeated_first[0]) % repeated_diff[0]

          repeated_extra_highest = highest
          repeated_goal = count + repeated_extra_counts

          # pp((repeated_extra_counts, count, repeated_extra_highest, repeated_goal))

  else:
    rr = new_rr_2

# print_dgrid(dg, y_start_at_top=False)

ans = highest + 1
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
