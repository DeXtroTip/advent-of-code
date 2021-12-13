# flake8: noqa

import sys

from utils.all import *

YEAR = 2020
DAY = 1

if 'x' in sys.argv:
  fin = aoc.get_input(DAY, example=True)
else:
  fin = aoc.get_input(DAY)

try:
  ints = get_ints(fin)
except:
  pass

###

ans = None

for x in ints:
  if ans is None:
    for y in ints[1:]:
      if x + y == 2020:
        ans = x * y
        break

aoc.print_answer(ans, 1)
aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = None

for x in ints:
  if ans is None:
    for y in ints[1:]:
      if ans is None:
        for z in ints[2:]:
          if x + y + z == 2020:
            ans = x * y * z
            break

aoc.print_answer(ans, 2)
aoc.submit_answer(ans, 2, DAY, YEAR)
