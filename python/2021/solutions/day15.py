from itertools import product

from utils import aoc
from utils.algorithms import dgrid_coord_ranges, dijkstra_cost
from utils.helpers import get_dgrid, graph_from_dgrid

YEAR, DAY = 2021, 15

fin = aoc.get_input(DAY)
dg = get_dgrid(fin, cast=int)

g = graph_from_dgrid(dg)
target = dgrid_coord_ranges(dg)[1]
aoc.print_answer(dijkstra_cost(g, (0, 0), target), 1)

xs = target[0] + 1
ys = target[1] + 1

for i, j in product(range(5), range(5)):
  if i == 0 and j == 0:
    continue
  for x, y in product(range(xs), range(ys)):
    new_pos = (x + xs * i, y + ys * j)
    dg[new_pos] = (dg[x, y] + i + j) % 9
    if not dg[new_pos]:
      dg[new_pos] = 9

g = graph_from_dgrid(dg)
target = dgrid_coord_ranges(dg)[1]
aoc.print_answer(dijkstra_cost(g, (0, 0), target), 2)
