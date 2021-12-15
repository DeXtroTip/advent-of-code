# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 15

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  return line


try:
  fin = aoc.get_input(DAY, example=DEBUG)
  ints = get_ints(fin)
except:
  pass

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  lines = get_lines(fin, parse_pattern=None)
except:
  lines = None
finally:
  if lines is not None:
    plines = [parse_line(line) for line in lines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  g = get_matrix(fin, cast=int)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

###

ans = 0
#

goal = (len(lines[0]) - 1, len(lines) - 1)

risks = set()

pr = {(0, 0): 0}

dq = deque()
dq.append(((0, 0), 0))
while dq:
  p, tw = dq.popleft()

  if pr[p] < tw:
    continue

  for move in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    np = element_sum(p, move)
    if np not in g:
      continue
    nw = tw + g[np]

    if np == goal:
      risks.add(nw)
      continue

    currw = pr.get(np, nw + 1)
    if nw > currw:
      continue
    pr[np] = nw
    dq.append((np, nw))

ans = min(risks)
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = 0
#

xs = len(lines[0])
ys = len(lines)

min_x = int(min(g.keys(), key=lambda p: p[0])[0])
max_x = int(max(g.keys(), key=lambda p: p[0])[0])
min_y = int(min(g.keys(), key=lambda p: p[1])[1])
max_y = int(max(g.keys(), key=lambda p: p[1])[1])
for y in range(min_y, max_y + 1):
  for x in range(min_x, max_x + 1):
    for i in range(1, 5):
      np = (x + xs * i, y)
      npp = (x + xs * (i - 1), y)
      nv = (g[npp] + 1) % 10
      if not nv:
        nv += 1
      g[np] = nv

min_x = int(min(g.keys(), key=lambda p: p[0])[0])
max_x = int(max(g.keys(), key=lambda p: p[0])[0])
for x in range(min_x, max_x + 1):
  for y in range(min_y, max_y + 1):
    for i in range(1, 5):
      np = (x, y + ys * i)
      npp = (x, y + ys * (i - 1))
      nv = (g[npp] + 1) % 10
      if not nv:
        nv += 1
      g[np] = nv

# print_matrix(g)

goal = (len(lines[0]) * 5 - 1, len(lines) * 5 - 1)

G = nx.DiGraph()
for p, w in g.items():
  for move in ((0, 1), (1, 0), (0, -1), (-1, 0)):
    np = element_sum(p, move)
    if np not in g:
      continue
    w = g[np]
    G.add_edge(p, np, weight=w)

g[(0, 0)] = 0
path = nx.shortest_path(G, source=(0, 0), target=goal, weight='weight')

#
ans = sum(g[x] for x in path)
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
