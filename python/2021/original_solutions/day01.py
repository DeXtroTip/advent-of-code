# flake8: noqa

from utils import *

fin = aoc.get_input(1)
fin = list(map(int, fin))

total = 0
prev = None
for i, line in enumerate(fin):
  if prev is not None and line > prev:
    total += 1
  prev = line
aoc.print_answer(total, 1)
aoc.submit_answer(total, 1)

total = 0
prev = [fin[0], fin[1], fin[2]]
for i, line in enumerate(fin[3:]):
  t = prev + [line]
  if len(t) > 3:
    t = t[1:]
  if sum(t) > sum(prev):
    total += 1
  prev = t
aoc.print_answer(total, 2)
aoc.submit_answer(total, 2)
