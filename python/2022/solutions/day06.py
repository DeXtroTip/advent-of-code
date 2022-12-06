from collections import deque
from itertools import islice

from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 6

fin = aoc.get_input(DAY)
datastream = get_lines(fin)[0]

last = deque()
ans1 = None
ans2 = None

for n, c in enumerate(datastream, 1):
  if len(last) >= 14:
    last.pop()
  last.appendleft(c)

  if not ans1 and len(set(islice(last, 0, 4))) == 4:
    ans1 = n
  if not ans2 and len(set(last)) == 14:
    ans2 = n
  if ans1 and ans2:
    break

aoc.submit_handler(ans1, part=1, day=DAY, year=YEAR, skip_confirmation=True)
aoc.submit_handler(ans2, part=2, day=DAY, year=YEAR, skip_confirmation=True)
