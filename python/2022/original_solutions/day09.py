# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 9

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  # return line

  # tokens = [t for t in line.split(' ')]
  # return tokens

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
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

if DEBUG:
  # print_dgrid(dg)
  # pp(plines)
  pass

### part 1

D_MAP = {
  'U': (0, -1),
  'D': (0, 1),
  'R': (1, 0),
  'L': (-1, 0),
}

dg = {(0, 0): 'H'}
places = {(0, 0)}

head = (0, 0)
tail = (0, 0)

for i, line in enumerate(plines):
  d, dis = line
  dm = D_MAP[d]
  for _ in range(dis):
    ntail = tail
    nhead = element_sum(head, dm)
    dg[nhead] = 'H'
    dg[head] = '.'
    if head == tail:
      dg[tail] = 'T'

    if nhead == tail:
      pass
    elif 'H' not in dgrid_neighbors8_values(dg, tail, default='.'):
      ntail = head
      dg[ntail] = 'T'
      dg[tail] = '.'
    tail = ntail
    head = nhead
    places.add(tail)
    # print_dgrid(dg)
    # print()

ans = len(places)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

dg = {(0, 0): 0}
places = {(0, 0)}

knots = list(range(0, 10))
knots_pos = defaultdict(lambda: (0, 0))

for line in plines:
  d, dis = line
  dm = D_MAP[d]

  for _ in range(dis):
    # print_dgrid(dg)
    # print()
    for knot in knots:
      p = knots_pos[knot]
      if knot == 0:
        new_p = element_sum(p, dm)
        knots_pos[knot] = new_p
        dg[new_p] = knot
        dg[p] = '.'
        for k in knots[knot + 1:]:
          if knots_pos[k] == p:
            dg[p] = k
            break
      else:
        follow = knots[knot - 1]
        if knots_pos[follow] == p:
          continue
        if knots_pos[follow] not in dgrid_neighbors8(dg, p):
          x, y = p
          fx, fy = knots_pos[follow]
          if x == fx:
            m = 1 if fy > y else -1
            new_p = (x, y + m)
          elif y == fy:
            m = 1 if fx > x else -1
            new_p = (x + m, y)
          else:
            mx = 1 if fx > x else -1
            my = 1 if fy > y else -1
            new_p = (x + mx, y + my)
          knots_pos[knot] = new_p

          qq = dg.get(new_p, '.')
          if qq == '.' or qq < knot:
            dg[new_p] = knot
          dg[p] = '.'
          for k in knots[knot + 1:]:
            if knots_pos[k] == p:
              dg[p] = k
              break
      if knot == 9:
        places.add(knots_pos[knot])

# pp(places)

ans = len(places)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
