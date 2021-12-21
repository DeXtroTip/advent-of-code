# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 21

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
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
  # g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

start1 = int(lines[0].split(' ')[-1])
start2 = int(lines[1].split(' ')[-1])

### part 1

scores = [0, 0]
pos = [start1, start2]
roll = 0

curr = 0
GOAL = 1000
while True:
  print(scores, pos, roll, curr)

  if scores[0] >= GOAL:
    break
  if scores[1] >= GOAL:
    break

  for x in range(roll + 1, roll + 4):
    pos[curr] += x

  pos[curr] = pos[curr] % 10
  if pos[curr] == 0:
    pos[curr] = 10
  scores[curr] += pos[curr]
  roll += 3

  curr ^= 1

print(roll)
print(scores)
ans = min(scores) * roll
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

GOAL = 21
splits = deque([((0, 0), (start1, start2), 0)])

cache = {}
rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@lru_cache()
def f(scores, pos, curr):
  if scores[0] >= GOAL:
    return 1, 0
  if scores[1] >= GOAL:
    return 0, 1

  t1, t2 = 0, 0
  for r, c in rolls.items():
    npos = [pos[0], pos[1]]
    nscores = [scores[0], scores[1]]

    npos[curr] += r
    npos[curr] = npos[curr] % 10
    if npos[curr] == 0:
      npos[curr] = 10

    nscores[curr] += npos[curr]

    xx, yy = f(tuple(nscores), tuple(npos), curr ^ 1)
    t1 += xx * c
    t2 += yy * c

  return t1, t2


wins = f((0, 0), (start1, start2), 0)
print(wins)
ans = max(wins)
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
