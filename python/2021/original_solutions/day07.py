# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 7

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = [int(n) for n in get_lines(fin)[0].split(',')]


def part1(inp):
  costs = {}
  mmin = min(inp)
  mmax = max(inp)
  for c in range(mmin, mmax + 1):
    costs[c] = 0
    for v in inp:
      costs[c] += abs(v - c)
  return min(costs.values())


def part2(inp):
  costs = {}
  mmin = min(inp)
  mmax = max(inp)
  for c in range(mmin, mmax + 1):
    costs[c] = 0
    for v in inp:
      costs[c] += sum(range(0, abs(v - c) + 1))
  return min(costs.values())


p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
