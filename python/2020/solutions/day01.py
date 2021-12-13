from utils import aoc
from utils.helpers import get_ints

YEAR = 2020
DAY = 1

fin = aoc.get_input(DAY)

numbers = get_ints(fin)

found = set()
for x in numbers:
  y = 2020 - x
  if y in found:
    ans = x * y
    break
  found.add(x)

aoc.print_answer(ans, 1)

ans = None
found = []
for x in numbers:
  yz = 2020 - x

  if ans is None:
    for i, y in enumerate(found):
      z = yz - y
      if z in found[i + 1:]:
        ans = x * y * z
        break
  found.append(x)

aoc.print_answer(ans, 2)
