from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2021, 17

fin = aoc.get_input(DAY)
x1, x2, y1, y2 = [int(n) for n in get_lines(fin, regex=r'target area: x=(\d+)\.\.(\d+), y=(-\d+)..(-\d+)')[0]]


def f(vx, vy):
  maxy = 0
  px, py = 0, 0
  while px <= x2 and py >= y1:
    px, py = px + vx, py + vy
    vx, vy = max(0, vx - 1), vy - 1
    maxy = max(maxy, py)
    if x1 <= px <= x2 and y1 <= py <= y2:
      return maxy
  return None


vel_top = {}
for x in range(x2 + 1):
  for y in range(y1, abs(y1)):
    maxy = f(x, y)
    if maxy is not None:
      vel_top[(x, y)] = maxy

aoc.print_answer(max(vel_top.values()), 1)
aoc.print_answer(len(vel_top), 2)
