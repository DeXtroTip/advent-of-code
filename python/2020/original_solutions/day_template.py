# flake8: noqa

import sys

from utils.all import *

YEAR = 2020
DAY = 0

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

ans = ans
aoc.print_answer(ans, 1)
# aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = 0

ans = ans
aoc.print_answer(ans, 2)
# aoc.submit_answer(ans, 2, DAY, YEAR)
