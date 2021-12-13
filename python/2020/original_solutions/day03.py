# flake8: noqa

import sys

from utils.all import *

YEAR = 2020
DAY = 3

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  return line


try:
  ints = get_ints(fin)
except:
  fin = aoc.get_input(DAY, example=DEBUG)
  try:
    lines = get_lines(fin, parse_pattern=None)
    lines = [parse_line(line) for line in lines]
  except:
    fin = aoc.get_input(DAY, example=DEBUG)

###

ans = 0

x, y = 0, 0
while y < len(lines):
  if lines[y][x] == '#':
    ans += 1
  x = (x + 3) % len(lines[y])
  y += 1

aoc.print_answer(ans, 1)
aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = []

for sx, sy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
  tmp = 0
  x, y = 0, 0
  while y < len(lines):
    if lines[y][x] == '#':
      tmp += 1
    x = (x + sx) % len(lines[y])
    y += sy
  ans.append(tmp)

ans = math.prod(ans)
aoc.print_answer(ans, 2)
aoc.submit_answer(ans, 2, DAY, YEAR)
