# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 5

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def parse_line(line):
  t1, t2 = line.split('->')
  a, b = [int(n) for n in t1.split(',')]
  c, d = [int(n) for n in t2.split(',')]
  return a, b, c, d


def part1():
  g = {}
  for i, line in enumerate(DATA_INPUT):
    x1, y1, x2, y2 = parse_line(line)

    if x1 != x2 and y1 == y2:
      if x1 > x2:
        for k in range(x2, x1 + 1, 1):
          g[(k, y1)] = g.get((k, y1), 0) + 1
      elif x2 > x1:
        for k in range(x1, x2 + 1, 1):
          g[(k, y1)] = g.get((k, y1), 0) + 1
    elif y1 != y2 and x1 == x2:
      if y1 > y2:
        for k in range(y2, y1 + 1, 1):
          g[(x1, k)] = g.get((x1, k), 0) + 1
      elif y2 > y1:
        for k in range(y1, y2 + 1, 1):
          g[(x1, k)] = g.get((x1, k), 0) + 1
  return sum(x > 1 for x in g.values())


def part2():
  g = {}
  for i, line in enumerate(DATA_INPUT):
    x1, y1, x2, y2 = parse_line(line)

    if x1 != x2 and y1 == y2:
      if x1 > x2:
        for k in range(x2, x1 + 1, 1):
          g[(k, y1)] = g.get((k, y1), 0) + 1
      elif x2 > x1:
        for k in range(x1, x2 + 1, 1):
          g[(k, y1)] = g.get((k, y1), 0) + 1
    elif y1 != y2 and x1 == x2:
      if y1 > y2:
        for k in range(y2, y1 + 1, 1):
          g[(x1, k)] = g.get((x1, k), 0) + 1
      elif y2 > y1:
        for k in range(y1, y2 + 1, 1):
          g[(x1, k)] = g.get((x1, k), 0) + 1

    elif abs(x1 - x2) == abs(y1 - y2):
      if x1 > x2:
        if y1 > y2:
          for k, q in zip(range(x2, x1 + 1, 1), range(y2, y1 + 1, 1)):
            g[(k, q)] = g.get((k, q), 0) + 1
        else:
          for k, q in zip(range(x2, x1 + 1, 1), range(y2, y1 - 1, -1)):
            g[(k, q)] = g.get((k, q), 0) + 1
      elif x2 > x1:
        if y1 > y2:
          for k, q in zip(range(x1, x2 + 1, 1), range(y1, y2 - 1, -1)):
            g[(k, q)] = g.get((k, q), 0) + 1
        else:
          for k, q in zip(range(x1, x2 + 1, 1), range(y1, y2 + 1, 1)):
            g[(k, q)] = g.get((k, q), 0) + 1

  return sum(x > 1 for x in g.values())


p1 = part1()
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2()
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
