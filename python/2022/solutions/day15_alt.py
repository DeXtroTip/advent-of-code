import z3

from utils import aoc
from utils.algorithms import manhattan_dis
from utils.helpers import get_lines
from utils.solvers import z3_abs

YEAR, DAY = 2022, 15

fin = aoc.get_input(DAY)
lines = get_lines(fin, regex=r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', re_cast=int)

beacons = set()
sensors = {}
for sx, sy, bx, by in lines:
  sensors[(sx, sy)] = manhattan_dis((sx, sy), (bx, by))
  beacons.add((bx, by))

target_row = 2000000
filled = set()
for sensor, dis in sensors.items():
  sx, sy = sensor
  if not (sy - dis <= target_row <= sy + dis):
    continue
  k = dis - abs(target_row - sy)
  filled.update(range(sx - k, sx + k + 1))

ans = len(filled) - sum(by == target_row for _, by in beacons)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

search_range = (0, target_row * 2)
smin, smax = search_range

x, y = z3.Ints('x y')
solver = z3.Optimize()
solver.add(x >= smin, x <= smax, y >= smin, y <= smax)

for sensor, dis in sensors.items():
  sx, sy = sensor
  solver.add(dis < z3_abs(x - sx) + z3_abs(y - sy))

solver.check()
m = solver.model()
fx = m[x].as_long()
fy = m[y].as_long()

ans = fx * 4000000 + fy
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
