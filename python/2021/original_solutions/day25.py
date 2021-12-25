# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 25

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(pattern, line).fixed

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
    # plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  # g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

# pp(lines)

### part 1

for step in count(1, 1):
  min_x = int(min(dg.keys(), key=lambda p: p[0])[0])
  max_x = int(max(dg.keys(), key=lambda p: p[0])[0])
  min_y = int(min(dg.keys(), key=lambda p: p[1])[1])
  max_y = int(max(dg.keys(), key=lambda p: p[1])[1])

  used = set()
  moved = set()
  for c in ('>', 'v'):
    ndg = {**dg}
    for y in range(min_y, max_y + 1):
      for x in range(min_x, max_x + 1):
        if (x, y) in used:
          continue
        p = dg.get((x, y))
        if p == c:
          m = (1, 0) if c == '>' else (0, 1)
          np = element_sum((x, y), m)
          if np[0] > max_x:
            np = (0, np[1])
          if np[1] > max_y:
            np = (np[0], 0)
          npp = dg.get(np, '.')
          if npp == '.':
            ndg[np] = p
            ndg[(x, y)] = '.'
            moved.add(np)
            used.add(np)
          else:
            used.add((x, y))
    dg = {**ndg}

  # print(step)
  # print_dgrid(dg)
  # print()

  if not moved:
    break

ans = step
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)
