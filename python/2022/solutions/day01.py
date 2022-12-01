from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 1

fin = aoc.get_input(DAY)
lines = get_lines(fin) + ['']

calories = [0]
for line in lines:
  if not line:
    calories.append(0)
    total = 0
    continue
  calories[-1] += int(line)
calories.sort(reverse=True)

ans = calories[0]
aoc.print_answer(ans, 1)

ans = sum(calories[:3])
aoc.print_answer(ans, 2)
