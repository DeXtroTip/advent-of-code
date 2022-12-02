# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 2

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  # return line

  tokens = [t for t in line.split(' ')]
  # return tokens

  pattern = '{} {}'
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

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

lines = plines[0]

if DEBUG:
  # print_dgrid(dg)
  # pp(plines)
  pass

### part 1

s1 = {
  'A': 1,
  'B': 2,
  'C': 3,
}
s2 = {
  'X': 1,
  'Y': 2,
  'Z': 3,
}

t1 = []
t2 = []
for line in plines:
  p1, p2 = line

  t1.append(s1[p1])
  t2.append(s2[p2])
  if p1 == 'A':
    if p2 == 'X':
      t1.append(3)
      t2.append(3)
    elif p2 == 'Y':
      t2.append(6)
    elif p2 == 'Z':
      t1.append(6)
  elif p1 == 'B':
    if p2 == 'X':
      t1.append(6)
    elif p2 == 'Y':
      t1.append(3)
      t2.append(3)
    elif p2 == 'Z':
      t2.append(6)
  elif p1 == 'C':
    if p2 == 'X':
      t2.append(6)
    elif p2 == 'Y':
      t1.append(6)
    elif p2 == 'Z':
      t1.append(3)
      t2.append(3)

ans = sum(t2)

aoc.print_answer(ans, 1)
if not DEBUG:
  yn = input("Submit part 1 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

wm = {
  ('A', 'X'): 'Z',
  ('A', 'Y'): 'X',
  ('A', 'Z'): 'Y',
  ('B', 'X'): 'X',
  ('B', 'Y'): 'Y',
  ('B', 'Z'): 'Z',
  ('C', 'X'): 'Y',
  ('C', 'Y'): 'Z',
  ('C', 'Z'): 'X',
}

total = 0
for line in plines:
  p1, p2 = line

  k = wm[(p1, p2)]
  a = s2[k]

  if p2 == 'X':
    b = 0
  elif p2 == 'Y':
    b = 3
  elif p2 == 'Z':
    b = 6

  total += a + b

ans = total

aoc.print_answer(ans, 2)
if not DEBUG:
  yn = input("Submit part 2 ? ('n' or Ctrl-c to cancel) ")
  if yn.lower() == 'n':
    sys.exit(0)
  aoc.submit_answer(ans, 2, DAY, YEAR)
