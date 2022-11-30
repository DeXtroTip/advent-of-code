# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2016, 2

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}\n'
  # tokens = parse.search(parse_pattern, line).fixed

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
    #plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

# pp(lines)

### part 1

ans = 0

m = {
  'U': (0, -1),
  'D': (0, 1),
  'L': (-1, 0),
  'R': (1, 0),
}
cm = {
  (0, 0): 1,
  (1, 0): 2,
  (2, 0): 3,
  (0, 1): 4,
  (1, 1): 5,
  (2, 1): 6,
  (0, 2): 7,
  (1, 2): 8,
  (2, 2): 9,
}

code = []
curr = (1, 1)
for line in lines:
  for c in line:
    move = m[c]
    curr = (min(max(curr[0] + move[0], 0), 2), min(max(curr[1] + move[1], 0), 2))
    # print(curr)
  code.append(str(cm[curr]))
  # print()

ans = ''.join(code)
aoc.print_answer(ans, 1)
if not DEBUG:
  yn = input("Submit part 1 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

cm = {
  (2, 0): '1',
  (1, 1): '2',
  (2, 1): '3',
  (3, 1): '4',
  (0, 2): '5',
  (1, 2): '6',
  (2, 2): '7',
  (3, 2): '8',
  (4, 2): '9',
  (1, 3): 'A',
  (2, 3): 'B',
  (3, 3): 'C',
  (2, 4): 'D',
}

code = []
curr = (0, 2)
for line in lines:
  for c in line:
    move = m[c]
    n_curr = element_sum(curr, move)
    if n_curr in cm:
      curr = n_curr
    # print(curr)
  code.append(str(cm[curr]))
  # print()

ans = ''.join(code)
aoc.print_answer(ans, 2)
if not DEBUG:
  yn = input("Submit part 2 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 2, DAY, YEAR)
