# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 12

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  return line

  tokens = [t for t in line.split(' ')]
  return tokens

  pattern = '{} {:d}'
  tokens = parse.search(pattern, line).fixed

  return tokens


try:
  fin = aoc.get_input(DAY, example=DEBUG)
  ints = get_ints(fin)
except:
  pass

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  lines = get_lines(fin, strip=True, parse_pattern=None)
except:
  lines = None
finally:
  if lines is not None:
    plines = [parse_line(line) for line in lines]
    # plines = [int(n) for n in plines]
    line = plines[0] if plines else None

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin,
                 cast=lambda c: 0 if c == 'S' else 27 if c == 'E' else ord(c) - ord('a') + 1,
                 y_start_at_top=True,
                 strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

if DEBUG:
  # print_dgrid(dg)
  # pp(plines)
  # pp(g)
  pass

### part 1

s = set()
d = {}
l = []

start = None
end = None

for pos, val in dg.items():
  if val == 0:
    start = pos
    dg[pos] = 1
  elif val == 27:
    end = pos
    dg[pos] = 26

# pp((start, end))

G = nx.DiGraph()
for p, w in dg.items():
  for move in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    np = element_sum(p, move)
    if np not in dg:
      continue
    nw = dg[np]
    if nw - w <= 1:
      # pp((p, np, w, nw))
      G.add_edge(p, np)

path = nx.shortest_path(G, source=start, target=end)
# pp(path)

ans = nx.shortest_path_length(G, source=start, target=end)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2
path = nx.shortest_path(G, source=start, target=end)
# pp(path)

sources = []
for pos, val in dg.items():
  if val == 1:
    sources.append(pos)

steps = []
for source in sources:
  try:
    steps.append(nx.shortest_path_length(G, source=source, target=end))
  except:
    pass

ans = min(steps)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
