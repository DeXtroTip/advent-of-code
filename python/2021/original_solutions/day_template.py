# flake8: noqa

from utils import *

YEAR = 2021
DAY = None

fin = aoc.get_input(DAY)

try:
  ints = get_ints(fin)
except:
  pass

###

ans = None
aoc.print_answer(ans, 1)
# aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = None
aoc.print_answer(ans, 2)
# aoc.submit_answer(ans, 2, DAY, YEAR)
