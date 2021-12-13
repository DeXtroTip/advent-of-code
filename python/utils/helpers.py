__all__ = [
  'get_ints',
  'get_lines',
]

import re


def get_ints(f):
  return list(map(int, f.readlines()))


def get_lines(f, regex=None, parse_pattern=None, strip=True):
  if parse_pattern is not None:
    import parse
    return [parse.search(parse_pattern, line.strip() if strip else line).fixed for line in f.readlines()]
  if regex is not None:
    return [re.compile(regex).findall(line.strip() if strip else line)[0] for line in f.readlines()]

  return [line.strip() if strip else line for line in f.readlines()]


def get_matrix(f, cast=None, start=(0, 0), y_start_at_top=True, strip=True):
  start_x, start_y = start
  m = {}

  lines = f.readlines()
  if not y_start_at_top:
    lines = lines[::-1]

  for i, line in enumerate(lines):
    if strip:
      line = line.strip()
    y = start_y + i
    for j, c in enumerate(line):
      x = start_x + j
      m[(x, y)] = c if cast is None else cast(c)

  return m


def print_matrix(matrix, default_val='.', mapping=None):
  if not matrix:
    return

  min_x = int(min(matrix.keys(), key=lambda p: p[0])[0])
  max_x = int(max(matrix.keys(), key=lambda p: p[0])[0])
  min_y = int(min(matrix.keys(), key=lambda p: p[1])[1])
  max_y = int(max(matrix.keys(), key=lambda p: p[1])[1])
  for y in range(min_y, max_y + 1):
    line = ''
    for x in range(min_x, max_x + 1):
      val = matrix.get((x, y), default_val)
      line += str(mapping.get(val, val) if mapping is not None else val)
    print(line)
