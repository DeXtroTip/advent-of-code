from utils import aoc
from utils.algorithms import dgrid_coord_ranges
from utils.helpers import get_dgrid

YEAR, DAY = 2022, 8

fin = aoc.get_input(DAY)

dg = get_dgrid(fin, cast=int)
(minx, miny), (maxx, maxy) = dgrid_coord_ranges(dg)

visible_count = 0
scenic_scores = set()

for pos, height in dg.items():
  x, y = pos
  is_visible = False

  if x == minx or x == maxx or y == miny or y == maxy:
    is_visible = True

  ranges = (
    (range(x - 1, minx - 1, -1), lambda k: (k, y)),  # noqa: B023
    (range(x + 1, maxx + 1), lambda k: (k, y)),  # noqa: B023
    (range(y - 1, miny - 1, -1), lambda k: (x, k)),  # noqa: B023
    (range(y + 1, maxy + 1), lambda k: (x, k)),  # noqa: B023
  )

  if not is_visible:
    is_visible = not all(any(dg[pos_function(coord)] >= height for coord in r) for r, pos_function in ranges)

  if is_visible:
    visible_count += 1

    score = 1
    for r, pos_function in ranges:
      _distance = 1
      for _distance, coord in enumerate(r, 1):
        if dg[pos_function(coord)] >= height:
          break
      score *= _distance
    scenic_scores.add(score)

ans = visible_count
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

ans = max(scenic_scores)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
