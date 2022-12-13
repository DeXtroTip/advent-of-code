from functools import cmp_to_key
from math import prod

from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 13

fin = aoc.get_input(DAY)
lines = [eval(line) for line in get_lines(fin) if line]


def compare(l1, l2):
  for a, b in zip(l1, l2):
    if isinstance(a, int) and isinstance(b, int):
      v = b - a
    else:
      v = compare(a if isinstance(a, list) else [a], b if isinstance(b, list) else [b])
    if v != 0:
      return v
  return len(l2) - len(l1)


ans = sum(idx for idx, i in enumerate(range(0, len(lines), 2), 1) if compare(lines[i], lines[i + 1]) > 0)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

new_elements = ([[2]], [[6]])
lines.extend(new_elements)
lines.sort(key=cmp_to_key(compare), reverse=True)

ans = prod(i for i, line in enumerate(lines, 1) if line in new_elements)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
