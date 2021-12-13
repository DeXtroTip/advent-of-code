# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 13

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)

def parse_line(line):
  if line.startswith('fold along'):
    tokens = line.split(' ')[2]
    t1, t2 = tokens.split('=')
    return t1, int(t2), True
  else:
    tokens = (int(t) for t in line.split(','))
    return *tokens, False


def get_printable_map(map_, default_val='.', mapping=None) -> str:
  """Get a map in a printable way for a given map of FrozenPoints (2D int only) and mapping of values."""
  if len(map_) == 0:
    return ''
  out = ''
  min_x = int(min(point[0] for point in map_.keys()))
  max_x = int(max(point[0] for point in map_.keys()))
  min_y = int(min(point[1] for point in map_.keys()))
  max_y = int(max(point[1] for point in map_.keys()))
  for y_coord in range(min_y, max_y + 1):
    line = ''
    for x_coord in range(min_x, max_x + 1):
      map_val = map_.get((x_coord, y_coord), default_val)
      line += str(mapping.get(map_val, map_val) if mapping is not None else map_val)
    out += line + '\n'
  return out


def fold(g, x_or_y, v):
  min_x = 0
  max_x = int(max(point[0] for point in g.keys()))
  min_y = 0
  max_y = int(max(point[1] for point in g.keys()))
  ng = {}
  if x_or_y == 0:  # y
    for i in range(max_y, v, -1):
      for x in range(min_x, max_x + 1):
        p = (x, i)
        op = (x, abs(i - v - v))
        if p in g:
          g[op] = g[op] if g.get(op) == '#' else g[p]
          del g[p]
    for y in range(min_y, v):
      for x in range(min_x, max_x + 1):
        ng[(x, y)] = g.get((x, y), '.')

  else:
    for i in range(max_x, v - 1, -1):
      for y in range(min_y, max_y + 1):
        p = (i, y)
        op = (abs(i - v - v), y)
        if p in g:
          g[op] = g[op] if g.get(op) == '#' else g[p]
          del g[p]
    for x in range(min_x, v):
      for y in range(min_y, max_y + 1):
        ng[(x, y)] = g.get((x, y), '.')

  for p in g.keys():
    if p not in ng:
      del g[p]


def part1(data_input):
  ans = None

  g = {}
  for i, line in enumerate(data_input):
    if not line:
      continue
    t1, t2, is_fold = parse_line(line)
    if not is_fold:
      g[(t1, t2)] = '#'
    else:
      fold(g, 1 if t1 == 'x' else 0, t2)
      break

  ans = sum(v == '#' for v in g.values())
  return ans


def part2(data_input):
  ans = None

  g = {}
  for i, line in enumerate(data_input):
    if not line:
      continue
    t1, t2, is_fold = parse_line(line)
    if not is_fold:
      g[(t1, t2)] = '#'
    else:
      fold(g, 1 if t1 == 'x' else 0, t2)
  print(get_printable_map(g))
  ans = "PFKLKCFP"
  return ans



p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
if not DEBUG:
  input("Submit ? (Ctrl-c to cancel)")
  aoc.submit_answer(p1, 1, DAY, YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
if not DEBUG:
  input("Submit ? (Ctrl-c to cancel)")
  aoc.submit_answer(p2, 2, DAY, YEAR)
