# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 7

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

ds = {}
dirs = deque()
root = None
curr_dir = None

for i, line in enumerate(plines):
  if line.startswith('$'):
    if 'cd' in line:
      x = line.split(' ')[-1]
      if x == '..':
        curr_dir = curr_dir['parent']
      elif x == '/':
        if root is not None:
          curr_dir = root
        else:
          curr_dir = {'name': x, 'dirs': {}, 'files': []}
          root = curr_dir
      else:
        curr_dir = curr_dir['dirs'][x]
    else:
      continue
  else:
    # print(curr_dir)
    t = line.split(' ')
    if t[0] == 'dir':
      fd = t[1]
      curr_dir['dirs'][fd] = {'name': fd, 'dirs': {}, 'files': [], 'parent': curr_dir}
    else:
      size = int(t[0])
      f = t[1]
      curr_dir['files'].append((f, size))

sizes = []


def calc_size(d):
  size = 0
  for f in d['files']:
    size += f[1]
  for k, v in d['dirs'].items():
    size += calc_size(v)
  sizes.append((d, size))
  return size


topd = root
# pp(topd)
root_size = calc_size(topd)

total = 0
for d, s in sizes:
  if s <= 100000:
    total += s

ans = total
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

available = 70000000
goal = 30000000

available -= root_size
# pp(available)
missing = goal - available
# pp(missing)

sorted_sizes = sorted(sizes, key=lambda s: s[1])
# pp(sorted_sizes)

delete_size = 0
for d, s in sorted_sizes:
  if s >= missing:
    delete_size = s
    break

ans = delete_size
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
