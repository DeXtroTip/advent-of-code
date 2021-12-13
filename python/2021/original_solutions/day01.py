# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 1

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_ints(fin)


def part1():
  total = 0
  prev = None
  for i, line in enumerate(DATA_INPUT):
    if prev is not None and line > prev:
      total += 1
    prev = line
  return total


def part2():
  total = 0
  prev = [DATA_INPUT[0], DATA_INPUT[1], DATA_INPUT[2]]
  for i, line in enumerate(DATA_INPUT[3:]):
    t = prev + [line]
    if len(t) > 3:
      t = t[1:]
    if sum(t) > sum(prev):
      total += 1
    prev = t
  return total


p1 = part1()
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2()
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
