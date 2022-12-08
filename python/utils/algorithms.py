import heapq
import math
from collections import defaultdict


def dgrid_neighbors_gen(deltas):

  def f(dg, coord, only_existing=False):
    for delta in (deltas):
      neighbor = element_sum(coord, delta)
      if not only_existing or neighbor in dg:
        yield neighbor

  return f


def dgrid_neighbors_gen_values(deltas):

  def f(dg, coord, only_existing=False, default=None):
    for neighbor in dgrid_neighbors_gen(deltas)(dg, coord, only_existing):
      if default is not None and neighbor not in dg:
        yield default
      else:
        yield dg[neighbor]

  return f


dgrid_neighbors4 = dgrid_neighbors_gen(((0, 1), (1, 0), (0, -1), (-1, 0)))
dgrid_neighbors4x = dgrid_neighbors_gen(((1, 1), (1, -1), (-1, 1), (-1, -1)))
dgrid_neighbors8 = dgrid_neighbors_gen(((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)))

dgrid_neighbors4_values = dgrid_neighbors_gen_values(((0, 1), (1, 0), (0, -1), (-1, 0)))
dgrid_neighbors4x_values = dgrid_neighbors_gen_values(((1, 1), (1, -1), (-1, 1), (-1, -1)))
dgrid_neighbors8_values = dgrid_neighbors_gen_values(
  ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)))


def dgrid_elements_direction_gen(delta):

  def f(dg, coord):
    while True:
      coord = element_sum(coord, delta)
      if coord in dg:
        yield coord
      else:
        break

  return f


def dgrid_elements_direction_gen_values(delta):

  def f(dg, coord):
    for element in dgrid_elements_direction_gen(delta)(dg, coord):
      yield dg[element]

  return f


dgrid_elements_left = dgrid_elements_direction_gen((-1, 0))
dgrid_elements_right = dgrid_elements_direction_gen((1, 0))
dgrid_elements_up = dgrid_elements_direction_gen((0, -1))
dgrid_elements_down = dgrid_elements_direction_gen((0, 1))

dgrid_elements_left_values = dgrid_elements_direction_gen_values((-1, 0))
dgrid_elements_right_values = dgrid_elements_direction_gen_values((1, 0))
dgrid_elements_up_values = dgrid_elements_direction_gen_values((0, -1))
dgrid_elements_down_values = dgrid_elements_direction_gen_values((0, 1))


def dgrid_coord_ranges(dg):
  if not dg:
    return ()
  mins = []
  maxs = []
  for i in range(len(next(iter(dg.keys())))):
    mins.append(int(min(dg.keys(), key=lambda p: p[i])[i]))
    maxs.append(int(max(dg.keys(), key=lambda p: p[i])[i]))
  return tuple(mins), tuple(maxs)


def dijkstra_path(g, start, end=None):
  costs = defaultdict(lambda: math.inf)
  costs[start] = 0

  paths = {start: (start, )}
  visited = set()

  queue = []
  heapq.heappush(queue, (0, start, (start, )))
  while queue:
    curr_cost, curr_node, curr_path = heapq.heappop(queue)
    visited.add(curr_node)

    if curr_node == end:
      return paths[end]

    for adjacent, cost in g[curr_node]:
      if adjacent not in visited:
        new_cost = curr_cost + cost
        if new_cost < costs[adjacent]:
          costs[adjacent] = new_cost
          paths[adjacent] = curr_path + (adjacent, )
          heapq.heappush(queue, (new_cost, adjacent, paths[adjacent]))

  return paths[end] if end else paths


def dijkstra_cost(g, start, end=None):
  costs = defaultdict(lambda: math.inf)
  costs[start] = 0

  visited = set()

  queue = []
  heapq.heappush(queue, (0, start))
  while queue:
    curr_cost, curr_node = heapq.heappop(queue)
    visited.add(curr_node)

    if curr_node == end:
      return costs[end]

    for adjacent, cost in g[curr_node]:
      if adjacent not in visited:
        new_cost = curr_cost + cost
        if new_cost < costs[adjacent]:
          costs[adjacent] = new_cost
          heapq.heappush(queue, (new_cost, adjacent))

  return costs[end] if end else costs


def element_sum(*args):
  return tuple(map(sum, zip(*args)))


def element_prod(*args):
  return tuple(map(math.prod, zip(*args)))


def element_diff(p1, p2):
  return tuple(c2 - c1 for c1, c2 in zip(p1, p2))


def collections_intersect(*args):
  if not args:
    return set()
  s = args[0] if isinstance(args[0], set) else set(args[0])
  for el in args[1:]:
    s = s.intersection(el)
  return s


def manhattan_dis(p1, p2):
  return sum(abs(c2 - c1) for c1, c2 in zip(p1, p2))


def set_bit(value, bit):
  return value | (1 << bit)


def clear_bit(value, bit):
  return value & ~(1 << bit)


def bin_to_int(b):
  return int(b, 2)


def hex_to_bin(h, fill=4):
  return bin(int(h, 16))[2:].zfill(fill)


def rotate_dir4(direction, rotation):
  if rotation.lower() == 'r':
    return (direction[1], direction[0] * -1)
  if rotation.lower() == 'l':
    return (direction[1] * -1, direction[0])
  raise ValueError(f"Rotation {rotation!r} is not valid!")
