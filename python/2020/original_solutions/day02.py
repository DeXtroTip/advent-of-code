# flake8: noqa

import sys

from utils.all import *

YEAR = 2020
DAY = 2

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

try:
  # ints = get_ints(fin)
  pass
except:
  pass

lines = fin.readlines()

###
ans = 0

for line in lines:
  pattern = "{a}-{b} {c}: {d}\n"
  match = parse.search(pattern, line)
  a, b, c, d = (match.named[x] for x in ('a', 'b', 'c', 'd'))
  a = int(a)
  b = int(b)

  cc = Counter(d)
  if a <= cc[c] <= b:
    ans += 1

aoc.print_answer(ans, 1)
aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = 0

for line in lines:
  pattern = "{a}-{b} {c}: {d}\n"
  match = parse.search(pattern, line)
  a, b, c, d = (match.named[x] for x in ('a', 'b', 'c', 'd'))
  a = int(a)
  b = int(b)

  if sum(d[i - 1] == c for i in (a, b)) == 1:
    ans += 1

aoc.print_answer(ans, 2)
aoc.submit_answer(ans, 2, DAY, YEAR)
