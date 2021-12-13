# flake8: noqa

import sys

from utils.all import *

YEAR = 2020
DAY = 5

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

seats = {}
for line in lines:
  x, y = 0, 127
  for c in line[:7]:
    m = (y - x) // 2
    if c == 'F':
      y = x + m
    elif c == 'B':
      x = y - m
  row = x

  x, y = 0, 7
  for c in line[7:]:
    m = (y - x) // 2
    if c == 'L':
      y = x + m
    elif c == 'R':
      x = y - m
  col = x
  seats[row * 8 + col] = (row, col)

ans = max(seats.keys())
aoc.print_answer(ans, 1)
aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = 0

ids = set(seats.keys())
seats = set(seats.values())
for row in range(1, 127):
  for col in range(8):
    i = row * 8 + col
    if i not in ids and i + 1 in ids and i - 1 in ids:
      ans = i

ans = ans
aoc.print_answer(ans, 2)
aoc.submit_answer(ans, 2, DAY, YEAR)
