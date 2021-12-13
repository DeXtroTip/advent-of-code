# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2000, 0

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  return line


try:
  ints = get_ints(fin)
finally:
  fin = aoc.get_input(DAY, example=DEBUG)
try:
  lines = get_lines(fin, parse_pattern=None)
  lines = [parse_line(line) for line in lines]
finally:
  fin = aoc.get_input(DAY, example=DEBUG)
try:
  g = get_matrix(fin)
  g = get_matrix(fin, cast=int)
finally:
  fin = aoc.get_input(DAY, example=DEBUG)

###

ans = 0

ans = ans
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = 0

ans = ans
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
