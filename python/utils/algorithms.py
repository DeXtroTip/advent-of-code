import heapq
import math
from collections import defaultdict


def dgrid_neighbors_gen(deltas):

  def f(dg, coord):
    for delta in (deltas):
      neighbor = element_sum(coord, delta)
      if neighbor in dg:
        yield neighbor

  return f


def dgrid_neighbors_gen_values(deltas):

  def f(dg, coord):
    for neighbor in dgrid_neighbors_gen(deltas)(dg, coord):
      yield dg[neighbor]

  return f


dgrid_neighbors4 = dgrid_neighbors_gen(((0, 1), (1, 0), (0, -1), (-1, 0)))
dgrid_neighbors4x = dgrid_neighbors_gen(((1, 1), (1, -1), (-1, 1), (-1, -1)))
dgrid_neighbors8 = dgrid_neighbors_gen(((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)))

dgrid_neighbors4_values = dgrid_neighbors_gen_values(((0, 1), (1, 0), (0, -1), (-1, 0)))
dgrid_neighbors4x_values = dgrid_neighbors_gen_values(((1, 1), (1, -1), (-1, 1), (-1, -1)))
dgrid_neighbors8_values = dgrid_neighbors_gen_values(
  ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)))


def dgrid_coord_ranges(dg):
  if not dg:
    return tuple()
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


def set_bit(value, bit):
  return value | (1 << bit)


def clear_bit(value, bit):
  return value & ~(1 << bit)
