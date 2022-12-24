# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 24

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

DIR_MAP = {
  '>': (1, 0),
  '<': (-1, 0),
  'v': (0, 1),
  '^': (0, -1),
}

# print_dgrid(dg)

(minx, miny), (maxx, maxy) = dgrid_coord_ranges(dg)

START = (minx + 1, 0)
TARGET = (maxx - 1, maxy)

REPEAT_ON = lcm(maxx - minx - 1, maxy - miny - 1)
pp(REPEAT_ON)

# block above start and below target to avoid going that way
dg[(START[0], START[1] - 1)] = '#'
dg[(TARGET[0], TARGET[1] + 1)] = '#'

orig_dg = dg.copy()


def print_minute(minute, pos=None):
  dd = dg.copy()
  for k, v in dd.items():
    if v in ('>', '<', 'v', '^'):
      dd[k] = '.'

  if pos:
    dd[pos] = 'E'

  blizzards, snowflakes, _ = calc_state(minute)
  for b, d in blizzards:
    if b in snowflakes:
      continue
    dd[b] = d

  for s, c in snowflakes.items():
    dd[s] = c

  print_dgrid(dd)


states_cache = {
  0: (
    {(k, v)
     for k, v in dg.items() if v in ('>', '<', 'v', '^')},
    {},
    {k
     for k, v in dg.items() if v in ('>', '<', 'v', '^')},
  )
}


@lru_cache()
def calc_state(minute):
  minute = minute % REPEAT_ON
  if minute in states_cache:
    return states_cache[minute]

  blizzards, snowflakes, _ = calc_state(minute - 1)
  new_blizzards = set()
  new_snowflakes = {}
  occupied = defaultdict(int)
  for b, d in blizzards:
    move = DIR_MAP[d]
    nb = element_sum(b, move)
    is_wall = dg.get(nb, '.') == '#'
    if is_wall:
      if move == (1, 0):
        nb = (minx + 1, nb[1])
      elif move == (-1, 0):
        nb = (maxx - 1, nb[1])
      elif move == (0, 1):
        nb = (nb[0], miny + 1)
      elif move == (0, -1):
        nb = (nb[0], maxy - 1)
      else:
        raise ValueError
      # k = (move[0] * -1, move[1] * -1)
      # nb = element_sum(nb, k)
      # while dg.get(nb, '.') != '#':
      #   nb = element_sum(nb, k)
      # nb = element_sum(nb, move)

    occupied[nb] += 1

    new_blizzards.add((nb, d))

  for b, c in occupied.items():
    if c > 1:
      new_snowflakes[b] = c

  states_cache[minute] = new_blizzards, new_snowflakes, set(occupied.keys())

  return states_cache[minute]


def solve(dg, start, end, offset=0):
  blizzards, _, _ = calc_state(offset)
  track = {(start, tuple(blizzards))}
  queue = deque(((start, 0), ))
  while queue:
    curr_pos, minutes = queue.popleft()

    minutes += 1
    blizzards, snowflakes, occupied = calc_state(minutes + offset)
    tblizzards = tuple(blizzards)

    # stay in same place
    if curr_pos not in occupied and (curr_pos, tblizzards) not in track:
      track.add((curr_pos, tblizzards))
      queue.append((curr_pos, minutes))

    for adjacent in dgrid_neighbors4(dg, curr_pos):
      if adjacent == end:
        return [], minutes

      is_occupied = adjacent in occupied or dg.get(adjacent, '.') == '#' or adjacent == start
      if is_occupied:
        continue

      if (adjacent, tblizzards) in track:
        continue

      track.add((adjacent, tblizzards))
      queue.append((adjacent, minutes))

  return [], -1


# print_minute(0)
# print_minute(1)
# print_minute(2)
# print_minute(3)
# print_minute(0)
# print_minute(12)
# print_minute(24)

_, sm = solve(dg, START, TARGET)
ans = sm
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

_, sm1 = solve(dg, START, TARGET)
_, sm2 = solve(dg, TARGET, START, offset=sm1)
_, sm3 = solve(dg, START, TARGET, offset=sm1 + sm2)
ans = sm1 + sm2 + sm3
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
