# WIP: solution without external packages but it's too slow (around 100 seconds for part 2)

from utils import aoc
from utils.algorithms import manhattan_dis
from utils.helpers import get_lines

YEAR, DAY = 2022, 15

fin = aoc.get_input(DAY)
lines = get_lines(fin, regex=r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', re_cast=int)

sensors = {}
distances = {}
for sx, sy, bx, by in lines:
  sensors[(sx, sy)] = (bx, by)
  distances[(sx, sy)] = manhattan_dis((sx, sy), (bx, by))

target_row = 2000000
filled = set()
for sensor in sensors:
  dis = distances[sensor]
  sx, sy = sensor
  if not (sy - dis <= target_row <= sy + dis):
    continue
  k = dis - abs(target_row - sy)
  filled.update(range(sx - k, sx + k + 1))

ans = len(filled) - sum(by == target_row for _, by in set(sensors.values()))
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

search_range = (0, target_row * 2)
smin, smax = search_range

fx, fy = None, None

for sensor in sensors:
  dis = distances[sensor]
  sx, sy = sensor

  for rangex in (range(sx, sx + dis + 1), range(sx - dis, sx)):
    for x in rangex:
      if x < smin or x > smax:
        continue
      for y in (sy + (dis - abs(x - sx)) + 1, sy - (dis - abs(x - sx)) - 1):
        if y < smin or y > smax:
          continue
        is_out_of_range = True
        for scan_sensor in sensors:
          if sensor == scan_sensor:
            continue
          if manhattan_dis((x, y), scan_sensor) <= distances[scan_sensor]:
            is_out_of_range = False
            break
        if is_out_of_range:
          fx = x
          fy = y
          break

      if fx is not None and fy is not None:
        break
    if fx is not None and fy is not None:
      break
  if fx is not None and fy is not None:
    break

ans = fx * 4000000 + fy
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
