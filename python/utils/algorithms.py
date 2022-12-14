import heapq
import math
from collections import defaultdict, deque

from .structures import DefaultDict


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


def bfs(g, start, ends=None):
  if start in ends:
    return 0

  queue = deque(((0, start), ))
  seen = {start}
  while queue:
    curr_cost, curr_node = queue.popleft()
    for adjacent in g[curr_node]:
      if adjacent in seen:
        continue
      if adjacent in ends:
        return curr_cost + 1
      seen.add(adjacent)
      queue.append((curr_cost + 1, adjacent))
  return -1


def bfs_path(g, start, ends=None):
  if start in ends:
    return (start, )

  queue = deque(((start, (start, )), ))
  seen = {start}

  if ends is None:
    paths = {start: (start, )}

  while queue:
    curr_node, curr_path = queue.popleft()
    for adjacent in g[curr_node]:
      if adjacent in seen:
        continue
      if adjacent in ends:
        return curr_path + (adjacent, )
      seen.add(adjacent)
      queue.append((adjacent, curr_path + (adjacent, )))
      if ends is None:
        paths[adjacent] = curr_path + (adjacent, )
  return paths if ends is None else ()


def astar_cost(g, start, end=None, weighted=True, heuristic=lambda p1, p2: manhattan_dis(p1, p2)):
  if start in end:
    return 0

  heuristics = DefaultDict(lambda x: manhattan_dis(x, end))
  costs = defaultdict(lambda: math.inf)
  costs[start] = 0
  visited = set()
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    _, curr_node = heapq.heappop(queue)
    curr_cost = costs[curr_node]

    if curr_node == end:
      return curr_cost
    visited.add(curr_node)

    for adjacent in g[curr_node]:
      adjacent, cost = adjacent if weighted else adjacent, 1
      new_cost = curr_cost + cost
      if adjacent not in visited and new_cost < costs[adjacent]:
        estimated_cost = new_cost + heuristics[adjacent]
        costs[adjacent] = new_cost
        heapq.heappush(queue, (estimated_cost, adjacent))

  return costs if end is None else math.inf


def astar_path(g, start, end=None, weighted=True, heuristic=lambda p1, p2: manhattan_dis(p1, p2)):
  if start == end:
    return (start, )

  heuristics = DefaultDict(lambda x: manhattan_dis(x, end))
  costs = defaultdict(lambda: math.inf)
  costs[start] = 0
  visited = set()
  queue = []
  heapq.heappush(queue, (0, start))

  if end is None:
    paths = {start: (start, )}

  while queue:
    _, curr_node = heapq.heappop(queue)
    curr_cost = costs[curr_node]
    curr_path = paths[curr_node]

    if curr_node == end:
      return curr_path
    visited.add(curr_node)

    for adjacent in g[curr_node]:
      adjacent, cost = adjacent if weighted else adjacent, 1
      new_cost = curr_cost + cost
      if adjacent not in visited and new_cost < costs[adjacent]:
        estimated_cost = new_cost + heuristics[adjacent]
        costs[adjacent] = new_cost
        heapq.heappush(queue, (estimated_cost, adjacent))
        if end is None:
          paths[adjacent] = curr_path + (adjacent, )

  return paths if end is None else ()


def dijkstra_path(g, start, end=None, weighted=True):
  if start == end:
    return (start, )

  costs = defaultdict(lambda: math.inf)
  costs[start] = 0
  visited = set()
  queue = []
  heapq.heappush(queue, (0, start))

  if end is None:
    paths = {start: (start, )}

  while queue:
    _, curr_node = heapq.heappop(queue)
    curr_cost = costs[curr_node]
    curr_path = paths[curr_node]

    if curr_node == end:
      return curr_path
    visited.add(curr_node)

    for adjacent in g[curr_node]:
      adjacent, cost = adjacent if weighted else adjacent, 1
      new_cost = curr_cost + cost
      if adjacent not in visited and new_cost < costs[adjacent]:
        costs[adjacent] = new_cost
        heapq.heappush(queue, (new_cost, adjacent))
        if end is None:
          paths[adjacent] = curr_path + (adjacent, )


def dijkstra_cost(g, start, end=None, weighted=True):
  if start in end:
    return 0

  costs = defaultdict(lambda: math.inf)
  costs[start] = 0
  visited = set()
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    _, curr_node = heapq.heappop(queue)
    curr_cost = costs[curr_node]

    if curr_node == end:
      return curr_cost
    visited.add(curr_node)

    for adjacent in g[curr_node]:
      adjacent, cost = adjacent if weighted else adjacent, 1
      new_cost = curr_cost + cost
      if adjacent not in visited and new_cost < costs[adjacent]:
        costs[adjacent] = new_cost
        heapq.heappush(queue, (new_cost, adjacent))

  return costs if end is None else math.inf


def invert_graph(g, weighted=True):
  new_g = defaultdict(list)
  for node, adjacents in g.items():
    for adjacent in adjacents:
      if weighted:
        adjacent, cost = adjacent
        new_g[adjacent].append((node, cost))
      else:
        new_g[adjacent].append(node)
  return new_g


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
