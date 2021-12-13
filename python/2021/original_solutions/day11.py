# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 11

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def part1(data_input):
  d = {}
  for y, line in enumerate(data_input[::]):
    for x, e in enumerate(line):
      d[(x, y)] = int(e)

  goal = 100

  flashes = 0
  for _ in range(goal):
    dq = deque(d.keys())
    flashed = set()
    while dq:
      oc = dq.popleft()
      if oc in flashed:
        continue
      d[oc] += 1
      if d[oc] > 9:
        flashed.add(oc)
        flashes += 1
        d[oc] = 0
        for mx in range(-1, 2):
          for my in range(-1, 2):
            if (mx, my) == (0, 0):
              continue
            adj = element_sum(oc, (mx, my))
            if adj in d and adj not in flashed:
              dq.append(adj)

  return flashes


def part2(data_input):
  d = {}
  for y, line in enumerate(data_input[::]):
    for x, e in enumerate(line):
      d[(x, y)] = int(e)

  s = 0
  while True:
    s += 1
    dq = deque(d.keys())
    flashed = set()
    while dq:
      oc = dq.popleft()
      if oc in flashed:
        continue
      d[oc] += 1
      if d[oc] > 9:
        flashed.add(oc)
        d[oc] = 0
        for mx in range(-1, 2):
          for my in range(-1, 2):
            if (mx, my) == (0, 0):
              continue
            adj = element_sum(oc, (mx, my))
            if adj in d and adj not in flashed:
              dq.append(adj)
    if len(flashed) == len(d):
      return s


p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
