# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 22

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
  lines = get_lines(fin, strip=False, parse_pattern=None)
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

last = lines[-1][:-1]

start_x, start_y = 0, 0
dg = {}

for i, line in enumerate(lines):
  if line == '\n':
    break
  y = start_y + i
  for j, c in enumerate(line[:-1]):
    if c == ' ':
      continue
    x = start_x + j
    dg[(x, y)] = c

# print_dgrid(dg, default_val=' ')

moves = []
n = ''
for i, c in enumerate(last):
  if c in ('R', 'L'):
    moves.append(int(n))
    moves.append(c)
    n = ''
  else:
    n += c
moves.append(int(n))

# pp(moves)

curr = None

x = 0
y = 0
while True:
  if dg.get((x, y)) == '.':
    break
  x += 1

DIRS = {
  'R': {
    (1, 0): (0, 1),
    (-1, 0): (0, -1),
    (0, 1): (-1, 0),
    (0, -1): (1, 0),
  },
  'L': {
    (1, 0): (0, -1),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (0, -1): (-1, 0),
  }
}

FACES = {
  (1, 0): '>',
  (-1, 0): '<',
  (0, 1): 'v',
  (0, -1): '^',
}

(minx, miny), (maxx, maxy) = dgrid_coord_ranges(dg)

p = (x, y)
f = (1, 0)

dg[p] = FACES[f]


def calc_wall_passage(p, f):
  x, y = p
  if f == (1, 0):
    nx = minx
    v = dg.get((nx, y))
    while v is None:
      nx += 1
      v = dg.get((nx, y))
    return (nx, y)
  if f == (-1, 0):
    nx = maxx
    v = dg.get((nx, y))
    while v is None:
      nx -= 1
      v = dg.get((nx, y))
    return (nx, y)
  if f == (0, 1):
    ny = miny
    v = dg.get((x, ny))
    while v is None:
      ny += 1
      v = dg.get((x, ny))
    return (x, ny)
  if f == (0, -1):
    ny = maxy
    v = dg.get((x, ny))
    while v is None:
      ny -= 1
      v = dg.get((x, ny))
    return (x, ny)
  raise Exception


for move in moves:
  # print_dgrid(dg, default_val=' ')
  if isinstance(move, str):
    f = DIRS[move][f]
    dg[p] = FACES[f]
    continue
  for _ in range(move):
    np = element_sum(p, f)
    v = dg.get(np)
    if v == '#':
      break
    elif v in ('.', '>', '<', 'v', '^'):
      p = np
      dg[p] = FACES[f]
    elif v is None:
      np = calc_wall_passage(np, f)
      v = dg.get(np)
      if v == '#':
        break
      elif v in ('.', '>', '<', 'v', '^'):
        p = np
        dg[p] = FACES[f]
      else:
        raise ValueError

# print_dgrid(dg, default_val=' ')
# pp((p, f))

x, y = p
rf = 0 if f == (1, 0) else 1 if f == (0, 1) else 2 if f == (-1, 0) else 3

ans = 1000 * (y + 1) + 4 * (x + 1) + rf
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

CUBE_SIZE = 4 if DEBUG else 50

dg = {}

for i, line in enumerate(lines):
  if line == '\n':
    break
  y = start_y + i
  for j, c in enumerate(line[:-1]):
    if c == ' ':
      continue
    x = start_x + j
    dg[(x, y)] = c

if DEBUG:
  cube_side_start = {
    (8, 0): 1,
    (0, 4): 2,
    (4, 4): 3,
    (8, 4): 4,
    (8, 8): 5,
    (12, 8): 6,
  }
else:
  # TODO
  cube_side_start = {
    (50, 0): 1,
    (100, 0): 2,
    (50, 50): 3,
    (50, 100): 4,
    (0, 100): 5,
    (0, 150): 6,
  }

cube_side_inv = {v: k for k, v in cube_side_start.items()}


def pos_cube_side(pos):
  x, y = pos
  xx = x - (x % CUBE_SIZE)
  yy = y - (y % CUBE_SIZE)
  return cube_side_start[(xx, yy)]


def calc_next_pos(p, f):
  x, y = p
  cube_side = pos_cube_side(p)
  cube_start = cube_side_inv[cube_side]

  pos_ref_cube = (x - cube_start[0], y - cube_start[1])
  refx, refy = pos_ref_cube

  # pp((p, cube_side, cube_start, pos_ref_cube))

  if DEBUG:
    if cube_side == 1:
      if f == (1, 0):
        next_cube = 6
        ref_pos = (CUBE_SIZE - 1, CUBE_SIZE - refy - 1)
        new_f = (-1, 0)
      elif f == (-1, 0):
        next_cube = 3
        ref_pos = (refy, 0)
        new_f = (0, 1)
      elif f == (0, 1):
        next_cube = 5
        ref_pos = (refx, CUBE_SIZE - 1)
        new_f = f
      # elif f == (0, -1):
      #   next_cube = 4
      #   ref_pos = (refx, 0)
      #   new_f = f
    elif cube_side == 2:
      # if f == (1, 0):
      #   next_cube = 3
      #   ref_pos = (0, refy)
      #   new_f = f
      if f == (-1, 0):
        next_cube = 6
        ref_pos = (refy, CUBE_SIZE - 1)
        new_f = (0, -1)
      elif f == (0, 1):
        next_cube = 5
        ref_pos = (refx, CUBE_SIZE - 1)
        new_f = (0, -1)
      elif f == (0, -1):
        next_cube = 1
        ref_pos = (refx, CUBE_SIZE - 1)
        new_f = f
    elif cube_side == 3:
      # if f == (1, 0):
      #   next_cube = 3
      #   ref_pos = (0, refy)
      #   new_f = f
      # elif f == (-1, 0):
      #   next_cube = 2
      #   ref_pos = (CUBE_SIZE - 1, refy)
      #   new_f = f
      if f == (0, 1):
        next_cube = 5
        ref_pos = (0, refx)
        new_f = (1, 0)
      elif f == (0, -1):
        next_cube = 1
        ref_pos = (0, refx)
        new_f = (1, 0)
    elif cube_side == 4:
      if f == (1, 0):
        next_cube = 6
        ref_pos = (CUBE_SIZE - refy - 1, 0)
        new_f = (0, 1)
      # elif f == (-1, 0):
      #   next_cube = 3
      #   ref_pos = (CUBE_SIZE - 1, refy)
      #   new_f = f
      # elif f == (0, 1):
      #   next_cube = 5
      #   ref_pos = (refx, 0)
      #   new_f = f
      # elif f == (0, -1):
      #   next_cube = 1
      #   ref_pos = (refx, CUBE_SIZE - 1)
      #   new_f = f
    elif cube_side == 5:
      # if f == (1, 0):
      #   next_cube = 6
      #   ref_pos = (0, refy)
      #   new_f = f
      if f == (-1, 0):
        next_cube = 3
        ref_pos = (CUBE_SIZE - 1 - refy, CUBE_SIZE - 1)
        new_f = (0, -1)
      elif f == (0, 1):
        next_cube = 2
        ref_pos = (CUBE_SIZE - 1 - refx, CUBE_SIZE - 1)
        new_f = (0, -1)
      # elif f == (0, -1):
      #   next_cube = 4
      #   ref_pos = (refx, CUBE_SIZE - 1)
      #   new_f = f
    elif cube_side == 6:
      if f == (1, 0):
        next_cube = 1
        ref_pos = (CUBE_SIZE - 1, CUBE_SIZE - 1 - refy)
        new_f = (-1, 0)
      # elif f == (-1, 0):
      #   next_cube = 5
      #   ref_pos = (CUBE_SIZE -1, refy)
      #   new_f = f
      elif f == (0, 1):
        next_cube = 2
        ref_pos = (0, CUBE_SIZE - 1 - refx)
        new_f = (1, 0)
      elif f == (0, -1):
        next_cube = 4
        ref_pos = (CUBE_SIZE - 1, CUBE_SIZE - 1 - refx)
        new_f = (-1, 0)
    else:
      raise ValueError
  else:
    if cube_side == 1:
      if f == (-1, 0):
        next_cube = 5
        ref_pos = (0, CUBE_SIZE - 1 - refy)
        new_f = (1, 0)
      elif f == (0, -1):
        next_cube = 6
        ref_pos = (0, refx)
        new_f = (1, 0)
    elif cube_side == 2:
      if f == (1, 0):
        next_cube = 4
        ref_pos = (CUBE_SIZE - 1, CUBE_SIZE - 1 - refy)
        new_f = (-1, 0)
      elif f == (0, 1):
        next_cube = 3
        ref_pos = (CUBE_SIZE - 1, refx)
        new_f = (-1, 0)
      elif f == (0, -1):
        next_cube = 6
        ref_pos = (refx, CUBE_SIZE - 1)
        new_f = (0, -1)
    elif cube_side == 3:
      if f == (1, 0):
        next_cube = 2
        ref_pos = (refy, CUBE_SIZE - 1)
        new_f = (0, -1)
      elif f == (-1, 0):
        next_cube = 5
        ref_pos = (refy, 0)
        new_f = (0, 1)
    elif cube_side == 4:
      if f == (1, 0):
        next_cube = 2
        ref_pos = (CUBE_SIZE - 1, CUBE_SIZE - 1 - refy)
        new_f = (-1, 0)
      elif f == (0, 1):
        next_cube = 6
        ref_pos = (CUBE_SIZE - 1, refx)
        new_f = (-1, 0)
    elif cube_side == 5:
      if f == (-1, 0):
        next_cube = 1
        ref_pos = (0, CUBE_SIZE - 1 - refy)
        new_f = (1, 0)
      elif f == (0, -1):
        next_cube = 3
        ref_pos = (0, refx)
        new_f = (1, 0)
    elif cube_side == 6:
      if f == (1, 0):
        next_cube = 4
        ref_pos = (refy, CUBE_SIZE - 1)
        new_f = (0, -1)
      elif f == (-1, 0):
        next_cube = 1
        ref_pos = (refy, 0)
        new_f = (0, 1)
      elif f == (0, 1):
        next_cube = 2
        ref_pos = (refx, 0)
        new_f = (0, 1)
    else:
      raise ValueError

  next_cube_start = cube_side_inv[next_cube]
  return element_sum(next_cube_start, ref_pos), new_f


#

x = 0
y = 0
while True:
  if dg.get((x, y)) == '.':
    break
  x += 1
p = (x, y)
f = (1, 0)

dg[p] = FACES[f]

combs_found = set()

for i, move in enumerate(moves, 1):
  # print_dgrid(dg, default_val=' ')

  sp = p
  sf = f
  G = 1777
  # if i == G:
  #   for k in dg:
  #     if dg[k] != '#':
  #       dg[k] = '.'

  #   dg[p] = FACES[f]
  #   print_dgrid(dg, default_val=' ')
  if isinstance(move, str):
    f = DIRS[move][f]
    dg[p] = FACES[f]
  else:
    for _ in range(move):
      np = element_sum(p, f)
      v = dg.get(np)
      if v == '#':
        break
      elif v in ('.', '>', '<', 'v', '^'):
        p = np
        dg[p] = FACES[f]
      elif v is None:
        np, nf = calc_next_pos(p, f)
        v = dg.get(np)
        if v == '#':
          break
        elif v in ('.', '>', '<', 'v', '^'):
          p = np
          f = nf
          dg[p] = FACES[f]
        else:
          raise ValueError
  # c1 = pos_cube_side(sp)
  # c2 = pos_cube_side(p)
  # if i > G and c1 != c2 and (c1, c2, sf, f) not in combs_found:
  #   pp((i, c1, c2, sf, f, sp, p))
  #   print_dgrid(dg, default_val=' ')
  #   break
  # combs_found.add((c1, c2, sf, f))

# print_dgrid(dg, default_val=' ')

# pp((p, f))

x, y = p
rf = 0 if f == (1, 0) else 1 if f == (0, 1) else 2 if f == (-1, 0) else 3

ans = 1000 * (y + 1) + 4 * (x + 1) + rf
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
