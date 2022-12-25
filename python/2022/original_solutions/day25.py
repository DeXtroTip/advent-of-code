# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 25

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
  # pp(plines)
  pass

### part 1

s = set()
d = {}
l = []

MAP = {'-': -1, '=': -2}
INV_MAP = {-1: '-', -2: '='}

cache = {}


def to_decimal(s):
  if s in cache:
    return cache[s]
  t = 0
  for b, x in enumerate(s[::-1]):
    bx = 5**b
    y = MAP[x] if x in MAP else int(x)
    t += bx * y
  cache[s] = t
  return t


def to_snafu(n):
  s = z3.Solver()

  bits = [z3.Int(f'b{i}') for i in range(32)]
  for b in bits:
    s.add(b >= -2, b <= 2)

  nums = []
  for i, b in enumerate(bits):
    v = 5**i * b
    nums.append(v)

  s.add(sum(nums) == n)
  s.push()
  pp(s.check())
  m = s.model()

  zeros = True
  res = ''
  for b in bits[::-1]:
    if zeros and m[b] == 0:
      continue
    zeros = False
    v = m[b]
    if v == -1:
      vx = '-'
    elif v == -2:
      vx = '='
    else:
      vx = str(v)
    res += vx

  return res

  # queue = deque((('2', '1', '0', '-', '=')))
  # while queue:
  #   curr = queue.popleft()

  #   dec = to_decimal(curr)
  #   if dec == n:
  #     return curr

  #   for x in ('2', '1', '0', '-', '='):
  #     y = x + curr
  #     dec = to_decimal(y)
  #     if dec == n:
  #       return y

  #     if dec > n:
  #       continue

  #     queue.append(x + curr)


# pp(to_snafu(20))

total = 0
for i, line in enumerate(plines):
  x = to_decimal(line)
  total += x

ans = to_snafu(total)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

s = set()
d = {}
l = []

for i, line in enumerate(plines):
  if not line:
    continue

  for j, col in enumerate(plines[i]):
    pass

  pass

ans = 0
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
