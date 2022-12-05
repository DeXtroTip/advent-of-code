# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 5

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
    plines = [parse_line(line)[:-1] for line in lines]
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

MAX_COL = 3 if DEBUG else 9
cols = [deque() for n in range(1, MAX_COL + 1)]

for line in plines:
  if not line:
    break
  for col, i in enumerate(range(1, len(line), 4), 1):
    if line[i].isdigit():
      break
    if line[i].strip():
      cols[col - 1].append(line[i])

for i, line in enumerate(plines):
  if not line.startswith('move'):
    continue

  pattern = 'move {:d} from {:d} to {:d}'
  n, a, b = parse.search(pattern, line).fixed

  for _ in range(n):
    k = cols[a - 1].popleft()
    cols[b - 1].appendleft(k)

ans = ''.join(col[0] for col in cols)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

MAX_COL = 3 if DEBUG else 9
cols = [deque() for n in range(1, MAX_COL + 1)]

for line in plines:
  if not line:
    break
  for col, i in enumerate(range(1, len(line), 4), 1):
    if line[i].isdigit():
      break
    if line[i].strip():
      cols[col - 1].append(line[i])

for i, line in enumerate(plines):
  if not line.startswith('move'):
    continue

  pattern = 'move {:d} from {:d} to {:d}'
  n, a, b = parse.search(pattern, line).fixed

  m = []
  for _ in range(n):
    m.append(cols[a - 1].popleft())
  for x in m[::-1]:
    cols[b - 1].appendleft(x)

ans = ''.join(col[0] for col in cols)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
