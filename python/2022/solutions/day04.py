from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 4

fin = aoc.get_input(DAY)
section_pairs = get_lines(fin)

overlaps_any = 0
overlaps_full = 0
for section_pair in section_pairs:
  a, b, x, y = (int(section) for pair in section_pair.split(',') for section in pair.split('-'))
  if (a <= x and b >= y) or (x <= a and y >= b):
    overlaps_full += 1
    overlaps_any += 1
  elif (a <= x and b >= x) or (a <= y and b >= y) or (x <= a and y >= a) or (y <= b and y >= b):
    overlaps_any += 1

aoc.print_answer(overlaps_full, 1)
aoc.print_answer(overlaps_any, 2)
