# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 21

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

numbers = {}
calcs = {}

for i, line in enumerate(plines):
  tokens = line.split(': ')
  t = tokens[0]
  if tokens[1].isdigit():

    numbers[t] = int(tokens[1])
  else:
    calcs[t] = tokens[1]


def solve(m):
  if m in numbers:
    return numbers[m]
  e = calcs[m]
  t = e.split(' ')
  x, o, y = t

  if m == 'root':
    a, b = solve(x), solve(y)
    return eval(f"{a} {o} {b}"), a, b
  return eval(f"{solve(x)} {o} {solve(y)}")


v, a, b = solve('root')
ans = int(v)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

calcs['root'] = calcs['root'].replace('+', '==')

r0, _, r1 = calcs['root'].split(' ')

GOAL = int(solve(r1))
pp(('GOAL:', GOAL))

del calcs[r1]
numbers[r1] = GOAL

variables = {}
for x in plines:
  t = x.split(': ')[0]
  if t != 'root':
    variables[t] = z3.Int(t)

s = z3.Optimize()

s.add(variables[r0] == GOAL)

for x, n in numbers.items():
  if x == 'humn':
    continue
  v = variables[x]
  s.add(v == n)

# pp(s)

for x, c in calcs.items():
  if x in ('root', r1):
    continue
  v = variables[x]
  a, o, b = c.split(' ')

  va = variables[a]
  vb = variables[b]

  if o == '+':
    s.add(v == va + vb)
  elif o == '-':
    s.add(v == va - vb)
  elif o == '*':
    s.add(v == va * vb)
  elif o == '/':
    s.add(v * vb == va)
  else:
    raise NotImplementedError

# pp(s)

s.push()
s.maximize(variables['humn'])
s.check()
model = s.model()
# pp(model)

ans = model[variables['humn']]

aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
