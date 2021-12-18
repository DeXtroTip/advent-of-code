# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 18

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  # return tokens
  return line


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
    #plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

elines = []
for line in lines:
  elines.append(eval(line))

a = []


def proc(el, level=1, arr=None):
  if arr is None:
    arr = []
  if isinstance(el, int):
    arr.append((el, level - 1))
  else:
    proc(el[0], level + 1, arr)
    proc(el[1], level + 1, arr)
  return arr


for el in elines:
  a.append(proc(el))
# print(a)

### part 1

# def xreduce(numbers, level=0):
#   if level == 5:
#     return True, numbers[0], numbers[1]
#   for i, p in enumerate(numbers):
#     print(p)
#     p1, p2 = p

#     if isinstance(p1, list):
#       exp, v1, v2 = xreduce(p1, level + 1)

#     else:
#       pass

#     if isinstance(p2, list):
#       exp, v1, v2 = xreduce(p2, level + 1)
#     else:
#       pass

#     print(numbers)


def xreduce2(arr, level=0):
  print("S", arr)

  narr = arr[::]
  while True:
    exploded = False
    split = False
    arr = narr[::]
    print(arr)
    for i, p1 in enumerate(arr[:-1]):
      j = i + 1
      p2 = arr[j]
      v1, lvl1 = p1
      v2, lvl2 = p2

      if lvl1 == lvl2 and lvl1 == 5:
        exploded = True
        narr = narr[:i] + [(0, lvl1 - 1)] + narr[i + 2:]
        if i > 0:
          prev = narr[i - 1]
          narr[i - 1] = (prev[0] + v1, prev[1])
        if j < len(narr):
          pnext = narr[j]
          narr[j] = (pnext[0] + v2, pnext[1])
        break

    if not exploded:
      for i, p in enumerate(arr):
        v, lvl = p

        if v > 9:
          split = True
          nv1 = v // 2
          if v % 2 == 0:
            nv2 = nv1
          else:
            nv2 = nv1 + 1
          narr = narr[:i] + [(nv1, lvl + 1), (nv2, lvl + 1)] + narr[i + 1:]
          break

    if not exploded and not split:
      break

  print("E", narr)
  return narr


def xsum(ns):
  n1 = ns[0] * 3 if isinstance(ns[0], int) else xsum(ns[0]) * 3
  n2 = ns[1] * 2 if isinstance(ns[1], int) else xsum(ns[1]) * 2
  return n1 + n2


def xsum2(arr):
  narr = arr[::]
  while len(narr) > 1:
    arr = narr[::]
    for i, p1 in enumerate(arr[:-1]):
      j = i + 1
      p2 = arr[i + 1]
      v1, lvl1 = p1
      v2, lvl2 = p2

      nv = v1 * 3 + v2 * 2

      if lvl1 == lvl2:
        narr = narr[:i] + [(nv, lvl1 - 1)] + narr[i + 2:]
        break

  return narr[0][0]


def sum_a(a1, a2):
  a = []
  for p in a1 + a2:
    a.append((p[0], p[1] + 1))
  return a


curr = a[0]
curr = xreduce2(curr)
print()
for ax in a[1:]:
  nx = sum_a(curr, ax)
  curr = xreduce2(nx)
  print()

print("F", curr)
print()

# el = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
# curr = proc(el)
# print(curr)

ans = xsum2(curr)
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

maxs = -math.inf
vs = {}
for i in range(0, len(elines)):
  for j in range(i + 1, len(elines)):
    xa = proc(elines[i])
    xb = proc(elines[j])
    xx = sum_a(xa, xb)
    xr = xreduce2(xx)
    xs = xsum2(xr)
    # maxs = max(maxs, xs)
    vs[(i, j)] = xs

pp(vs)
maxs = max(vs.values())
ans = maxs
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
