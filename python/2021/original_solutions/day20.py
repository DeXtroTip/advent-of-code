# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 20

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
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
  fin.readline()
  fin.readline()
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  # g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

xdg = defaultdict(int)
xdg.update(dg)
dg = xdg
iea = lines[0]
# print(iea)

### part 1

out = 0
for _ in range(2):
  # print_dgrid(dg)
  # print()

  min_x = int(min(dg.keys(), key=lambda p: p[0])[0]) - 1
  max_x = int(max(dg.keys(), key=lambda p: p[0])[0]) + 1
  min_y = int(min(dg.keys(), key=lambda p: p[1])[1]) - 1
  max_y = int(max(dg.keys(), key=lambda p: p[1])[1]) + 1

  ndg = defaultdict(int)
  ndg.update({k: v for k, v in dg.items()})
  curr_lighted = set()
  # print(dg)
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      v8x = list(dgrid_neighbors8_values(dg, (x, y), default=out))
      v8x.insert(4, dg[(x, y)] if (x, y) in dg else out)
      v8x = [1 if x == '#' else 0 if x == '.' else x for x in v8x]
      v = bin_to_int(''.join((str(x) for x in v8x)))
      if iea[v] == '#':
        curr_lighted.add((x, y))
      ndg[(x, y)] = iea[v]
      # print(x, y, v8x, v, iea[v])
      # print_dgrid(ndg)
      # print()

  out = 0 if out == 1 or iea[0] == '.' else 1

  dg = ndg

# print_dgrid(dg)
# print()

ans = sum(x == '#' for x in dg.values())
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

### part 2

fin = aoc.get_input(DAY, example=DEBUG)
fin.readline()
fin.readline()
dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
xdg = defaultdict(int)
xdg.update(dg)
dg = xdg

out = 0
for _ in range(50):
  # print_dgrid(dg)
  # print()

  min_x = int(min(dg.keys(), key=lambda p: p[0])[0]) - 1
  max_x = int(max(dg.keys(), key=lambda p: p[0])[0]) + 1
  min_y = int(min(dg.keys(), key=lambda p: p[1])[1]) - 1
  max_y = int(max(dg.keys(), key=lambda p: p[1])[1]) + 1

  ndg = defaultdict(int)
  ndg.update({k: v for k, v in dg.items()})
  curr_lighted = set()
  # print(dg)
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      v8x = list(dgrid_neighbors8_values(dg, (x, y), default=out))
      v8x.insert(4, dg[(x, y)] if (x, y) in dg else out)
      v8x = [1 if x == '#' else 0 if x == '.' else x for x in v8x]
      v = bin_to_int(''.join((str(x) for x in v8x)))
      if iea[v] == '#':
        curr_lighted.add((x, y))
      ndg[(x, y)] = iea[v]
      # print(x, y, v8x, v, iea[v])
      # print_dgrid(ndg)
      # print()

  out = 0 if out == 1 or iea[0] == '.' else 1

  dg = ndg

# print_dgrid(dg)
# print()

ans = sum(x == '#' for x in dg.values())
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
