# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 12

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def parse_line(line):
  tokens = [t for t in line.split('-')]
  return tokens


def part1(data_input):
  conns = defaultdict(list)
  for i, line in enumerate(data_input):
    t1, t2 = parse_line(line)
    conns[t1].append(t2)
    conns[t2].append(t1)

  big_caves = {x for x in conns.keys() if len(x) == 1 and x.isupper()}

  paths = []
  queue = deque((('start', ), ))
  while queue:
    currp = queue.popleft()
    lastc = currp[-1]
    for nextc in conns[lastc]:
      if nextc.islower() and nextc in currp:
        continue
      nn = currp + (nextc, )
      if 'end' in nn and all(c in currp for c in big_caves):
        paths.append(nn)
      else:
        queue.append(nn)

  return len(paths)


def part2(data_input):
  conns = defaultdict(list)
  for i, line in enumerate(data_input):
    t1, t2 = parse_line(line)
    conns[t1].append(t2)
    conns[t2].append(t1)

  paths = []
  queue = deque((('start', ), ))
  while queue:
    currp = queue.popleft()
    lastc = currp[-1]
    lowers_count = Counter((c for c in currp if c.islower()))
    any_max = any(c == 2 for c in lowers_count.values())
    for nextc in conns[lastc]:
      if nextc == 'start':
        continue
      if nextc.islower() and (lowers_count[nextc] == 2 or (lowers_count[nextc] == 1 and any_max)):
        continue
      nn = currp + (nextc, )
      if 'end' in nn:
        paths.append(nn)
      else:
        queue.append(nn)

  return len(paths)


p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
