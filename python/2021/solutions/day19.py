from collections import defaultdict
from itertools import product

from utils import aoc
from utils.algorithms import element_diff, element_prod, manhattan_dis
from utils.helpers import get_lines

YEAR, DAY = 2021, 19

PERMUTATIONS = (
  lambda p: (p[0], p[1], p[2]),
  lambda p: (p[0], p[2], p[1]),
  lambda p: (p[1], p[0], p[2]),
  lambda p: (p[1], p[2], p[0]),
  lambda p: (p[2], p[0], p[1]),
  lambda p: (p[2], p[1], p[0]),
)

DIRECTIONS = (
  (1, 1, 1),
  (-1, 1, 1),
  (1, -1, 1),
  (1, 1, -1),
  (-1, -1, 1),
  (-1, 1, -1),
  (1, -1, -1),
  (-1, -1, -1),
)


def orientations_gen():
  for permutation in PERMUTATIONS:
    for direction in DIRECTIONS:
      yield lambda p: element_prod(permutation(p), direction)


def points_relative_position(scanner):
  d = defaultdict(set)
  sorted_points = sorted(scanner)
  for p1, p2 in product(sorted_points, sorted_points):
    if p1 == p2:
      continue
    d[p1].add(tuple(c2 - c1 for c1, c2 in zip(p1, p2)))
  return d


fin = aoc.get_input(DAY)
lines = get_lines(fin)

scanners = []
for line in lines:
  if not line:
    continue
  if 'scanner' in line:
    scanners.append(set())
  else:
    scanners[-1].add(tuple(int(n) for n in line.split(',')))

beacons = scanners[0]
scanners_pos = {(0, 0, 0)}
scanners_found = {0}

while len(scanners_found) != len(scanners):
  for idx, scanner in enumerate(scanners):
    if idx in scanners_found:
      continue

    beacon_points_rpos = points_relative_position(beacons)

    for orientation_apply in orientations_gen():
      oriented_scanner = {orientation_apply(p) for p in scanner}
      scanner_points_rpos = points_relative_position(oriented_scanner)

      match_found = False
      for beacon_point, bp_distances in beacon_points_rpos.items():
        for scanner_point, sp_distances in scanner_points_rpos.items():

          beacons_overlap = 1 + len(bp_distances.intersection(sp_distances))
          if beacons_overlap >= 12:
            shift = element_diff(scanner_point, beacon_point)
            for beacon in oriented_scanner:
              beacons.add(tuple(c2 + c1 for c1, c2 in zip(beacon, shift)))
            scanners_pos.add(shift)
            scanners_found.add(idx)

            match_found = True
            break

        if match_found:
          break

      if match_found:
        break

aoc.print_answer(len(beacons), 1)

max_distance = max(manhattan_dis(s1, s2) for s1, s2 in product(scanners_pos, scanners_pos))
aoc.print_answer(max_distance, 2)
