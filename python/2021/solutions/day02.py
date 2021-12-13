from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2021, 2

fin = aoc.get_input(DAY)

lines = get_lines(fin, regex=r'(\w+) (\d+)')

horizontal = 0
depth = 0
for cmd, n in lines:
  n = int(n)
  if cmd == 'forward':
    horizontal += n
  elif cmd == 'down':
    depth += n
  elif cmd == 'up':
    depth -= n

aoc.print_answer(horizontal * depth, 1)

horizontal = 0
depth = 0
aim = 0
for cmd, n in lines:
  n = int(n)
  if cmd == 'forward':
    horizontal += n
    depth += (aim * n)
  elif cmd == 'down':
    aim += n
  elif cmd == 'up':
    aim -= n

aoc.print_answer(horizontal * depth, 2)
