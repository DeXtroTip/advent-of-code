# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 6

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = [int(n) for n in get_lines(fin)[0].split(',')]


def part1():
  state = DATA_INPUT[::]

  for _ in range(80):
    ns = []
    ns2 = []
    for f in state:
      if f == 0:
        f = 6
        ns2.append(8)
      else:
        f -= 1
      ns.append(f)
    state = ns + ns2

  return len(state)


def part2():
  fishes = DATA_INPUT[::]

  d = {x: 0 for x in range(9)}

  for f in fishes:
    d[f] += 1

  total = len(fishes)
  days = 256
  for _ in range(days):
    new = d[0]
    total += new

    for n in range(8):
      d[n] = d[n + 1]

    d[6] += new
    d[8] = new

  return total


p1 = part1()
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2()
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
