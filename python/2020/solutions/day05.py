from itertools import product

from utils import aoc
from utils.helpers import get_lines

YEAR = 2020
DAY = 5


def decode(low, high, code):
  for c in code:
    mid = (high - low) // 2
    if c in ('F', 'L'):
      high = low + mid
    else:
      low = high - mid
  return low


fin = aoc.get_input(DAY)
lines = get_lines(fin)

seats = set()
for line in lines:
  row = decode(0, 127, line[:7])
  col = decode(0, 7, line[7:])
  seats.add(row * 8 + col)

ans = max(seats)
aoc.print_answer(ans, 1)

for row, col in product(range(1, 127), range(0, 8)):
  seat = row * 8 + col
  if seat not in seats and seat + 1 in seats and seat - 1 in seats:
    ans = seat
    break

aoc.print_answer(ans, 2)
