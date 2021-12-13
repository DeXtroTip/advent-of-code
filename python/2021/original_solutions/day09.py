# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 9

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def part1(data_input):
  points = {}
  for y, line in enumerate(data_input):
    for x, c in enumerate(line):
      points[(x, y)] = int(c)

  risk = 0
  for p, val in points.items():
    flag = True
    for m in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      pp = element_sum(p, m)
      v = points.get(pp)
      if v is not None and v <= val:
        flag = False
        break
    if flag:
      risk += 1 + val
  return risk


def part2(data_input):
  points = {}
  for y, line in enumerate(data_input):
    for x, c in enumerate(line):
      points[(x, y)] = int(c)

  dq = deque()
  used = set()
  basinsm = {}
  basins = []
  for p, val in points.items():
    flag = True
    for m in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      pp = element_sum(p, m)
      v = points.get(pp)
      if v is not None and v <= val:
        flag = False
        break
    if flag:
      basins.append({p})
      basinsm[p] = len(basins) - 1
      used.add(p)
      dq.append(p)

  while dq:
    p = dq.popleft()
    val = points[p]
    basin_idx = basinsm[p]
    for m in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      pp = element_sum(p, m)
      if pp in used:
        continue
      v = points.get(pp)
      if v is not None and v != 9 and v > val:
        basins[basin_idx].add(pp)
        basinsm[pp] = basin_idx
        used.add(pp)
        dq.append(pp)

  t = 1
  for b in sorted(basins, key=len, reverse=True)[:3]:
    t *= len(b)
  return t


p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
