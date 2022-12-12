from utils import aoc
from utils.algorithms import dijkstra_cost
from utils.helpers import get_dgrid, graph_from_dgrid

YEAR, DAY = 2022, 12

fin = aoc.get_input(DAY)
heightmap = get_dgrid(fin, cast=lambda c: c if c in ('S', 'E') else ord(c) - ord('a') + 1)

source = None
target = None
start_elevations = []
for pos, height in heightmap.items():
  if height == 'S':
    source = pos
    heightmap[pos] = 1
  elif height == 'E':
    target = pos
    heightmap[pos] = 26

  if heightmap[pos] == 1:
    start_elevations.append(pos)

g = graph_from_dgrid(heightmap, weighted=False, edge_filter=lambda s, t, sw, tw: tw - sw <= 1)

ans = dijkstra_cost(g, source, target, weighted=False)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

ans = min(dijkstra_cost(g, start, target, weighted=False) for start in start_elevations)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
