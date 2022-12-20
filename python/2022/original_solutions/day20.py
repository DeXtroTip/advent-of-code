# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 20

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
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  is_weighted = True
  g = graph_from_dgrid(
    dg,
    weighted=is_weighted,
    neighbors=dgrid_neighbors4,
    weight_calc=lambda sw, tw: tw,
    edge_filter=lambda s, t, sw, tw: True,
  )
  G = graph_to_nx_digraph(g, weighted=is_weighted)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

if DEBUG:
  # print_dgrid(dg)
  # pp(ints)
  pass

### part 1

orig = ints.copy()


class Node:

  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None
    self.orig_next = None
    self.orig_prev = None


class LinkedList:

  def __init__(self):
    self.head = None


def print_list(head):
  vals = []
  curr = head
  for _ in range(len(orig)):
    vals.append(curr.val)
    curr = curr.next
  print(vals)


head = Node(ints[0])
prev = head

for n in ints[1:-1]:
  node = Node(n)
  node.orig_prev = node.prev = prev
  prev.orig_next = prev.next = node
  prev = node

last = Node(ints[-1])
prev.orig_next = prev.next = last
last.orig_prev = last.prev = prev

last.orig_next = last.next = head
head.orig_prev = head.prev = last

orig_head = head
curr = head
for i in range(len(orig)):
  v = curr.val

  aux = curr
  if v > 0:
    while v != 0:
      aux = aux.next
      if aux == curr:
        continue
      v -= 1
    if aux != curr:
      curr.prev.next, curr.next.prev = curr.next, curr.prev

      aux.next, curr.next = curr, aux.next
      curr.prev = aux
      curr.next.prev = curr
  elif v < 0:
    while v != 0:
      aux = aux.prev
      if aux == curr:
        continue
      v += 1
    if aux != curr:
      curr.prev.next, curr.next.prev = curr.next, curr.prev

      aux.prev, curr.prev = curr, aux.prev
      curr.next = aux
      curr.prev.next = curr

  # print_list(head)

  curr = curr.orig_next
  if curr == orig_head:
    break

curr = head
vals = []
while True:
  v = curr.val
  if v == 0:
    for i in range(1, 3001):
      curr = curr.next
      if i % 1000 == 0:
        vals.append(curr.val)
    break
  curr = curr.next

# pp(vals)

ans = sum(vals)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

KEY = 811589153

head = Node(ints[0] * KEY)
prev = head

for n in ints[1:-1]:
  node = Node(n * KEY)
  node.orig_prev = node.prev = prev
  prev.orig_next = prev.next = node
  prev = node

last = Node(ints[-1] * KEY)
prev.orig_next = prev.next = last
last.orig_prev = last.prev = prev

last.orig_next = last.next = head
head.orig_prev = head.prev = last

orig_head = head
for r in range(10):
  curr = head
  for i in range(len(orig)):
    v = curr.val
    v = abs(v) % (len(orig) - 1)
    if curr.val < 0:
      v = -v

    aux = curr
    if v > 0:
      while v != 0:
        aux = aux.next
        if aux == curr:
          continue
        v -= 1
      if aux != curr:
        curr.prev.next, curr.next.prev = curr.next, curr.prev

        aux.next, curr.next = curr, aux.next
        curr.prev = aux
        curr.next.prev = curr
    elif v < 0:
      while v != 0:
        aux = aux.prev
        if aux == curr:
          continue
        v += 1
      if aux != curr:
        curr.prev.next, curr.next.prev = curr.next, curr.prev

        aux.prev, curr.prev = curr, aux.prev
        curr.next = aux
        curr.prev.next = curr

    # print_list(head)

    curr = curr.orig_next
    if curr == orig_head:
      break

curr = head
vals = []
while True:
  v = curr.val
  if v == 0:
    for i in range(1, 3001):
      curr = curr.next
      if i % 1000 == 0:
        vals.append(curr.val)
    break
  curr = curr.next

# pp(vals)

ans = sum(vals)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
