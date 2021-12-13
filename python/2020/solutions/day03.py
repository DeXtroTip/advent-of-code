import math

from utils import aoc
from utils.helpers import get_lines

YEAR = 2020
DAY = 3

fin = aoc.get_input(DAY)
lines = get_lines(fin)

slopes = []
for sx, sy in ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2)):
  trees = 0
  for i, line in enumerate(lines[::sy]):
    x = (i * sx) % len(line)
    y = i * sy
    if line[x] == '#':
      trees += 1
  slopes.append(trees)

aoc.print_answer(slopes[0], 1)
aoc.print_answer(math.prod(slopes), 2)
