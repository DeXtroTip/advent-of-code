# WIP: not a clean solution yet, did not have time for more right now

from utils import aoc
from utils.algorithms import dgrid_neighbors8, element_sum
from utils.helpers import get_lines

YEAR, DAY = 2022, 9

fin = aoc.get_input(DAY)
lines = [tuple(int(t) if t.isdigit() else t for t in line.split(' ')) for line in get_lines(fin)]

D_MAP = {
  'U': (0, -1),
  'D': (0, 1),
  'R': (1, 0),
  'L': (-1, 0),
}


def solve(num_knots):
  dg = {(0, 0): 0, (5, -5): '.'}
  knots = [(0, 0) for _ in range(num_knots)]
  tail_visited = {(0, 0)}

  for line in lines:
    d, dis = line
    dm = D_MAP[d]

    for _ in range(dis):
      for knot, pos in enumerate(knots):
        x, y = pos

        if knot == 0:
          new_pos = element_sum(pos, dm)
          knots[knot] = new_pos
          dg[new_pos] = knot

          dg[pos] = '.'
          for k, kpos in enumerate(knots[knot + 1:], knot + 1):
            if kpos == pos:
              dg[kpos] = k
              break

        else:
          follow_knot = knot - 1
          follow_pos = knots[follow_knot]

          if follow_pos == pos:
            continue

          if follow_pos not in dgrid_neighbors8(dg, pos):
            fx, fy = follow_pos
            if x == fx:
              m = 1 if fy > y else -1
              new_pos = (x, y + m)
            elif y == fy:
              m = 1 if fx > x else -1
              new_pos = (x + m, y)
            else:
              mx = 1 if fx > x else -1
              my = 1 if fy > y else -1
              new_pos = (x + mx, y + my)

            knots[knot] = new_pos

            for k, kpos in enumerate(knots):
              if kpos == new_pos:
                dg[new_pos] = k
                break

            dg[pos] = '.'
            for k, kpos in enumerate(knots[knot + 1:], knot + 1):
              if kpos == pos:
                dg[kpos] = k
                break

          if knot == len(knots) - 1:
            tail_visited.add(knots[knot])

  return len(tail_visited)


aoc.submit_handler(solve(2), part=1, day=DAY, year=YEAR, skip_confirmation=True)
aoc.submit_handler(solve(10), part=2, day=DAY, year=YEAR, skip_confirmation=True)
