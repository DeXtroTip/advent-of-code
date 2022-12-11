# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 11

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
    plines = [parse_line(line) for line in lines] + ['']
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

s = set()
d = {}
l = []

monkeys = []

curr_monkey = {'inspects': 0}
for i, line in enumerate(plines):
  if not line:
    monkeys.append(curr_monkey)
    curr_monkey = {'inspects': 0}

  tokens = line.split(' ')

  if tokens[0] == 'Monkey':
    curr_monkey['id'] = int(tokens[1][:-1])
  elif tokens[0] == 'Starting':
    items = [int(t) for t in line.split(':')[1].split(',') if t]
    curr_monkey['items'] = items
  elif tokens[0] == 'Operation:':
    op = line.split('=')[1]
    op = op.replace('old', '{old}').strip()
    curr_monkey['op'] = op
  elif tokens[0] == 'Test:':
    val = int(tokens[-1])
    tests = []
    curr_monkey['test_in'] = val
  elif tokens[0] == 'If':
    val = int(tokens[-1])
    tests.append(val)
    curr_monkey['test_out'] = tests

r = 1

while True:
  for mid, monkey in enumerate(monkeys):
    if not monkey['items']:
      continue

    for item in monkey['items']:
      monkey['inspects'] += 1

      w = eval(monkey['op'].format(old=item))
      nw = math.floor(w / 3)

      if nw % monkey['test_in'] == 0:
        to = monkey['test_out'][0]
      else:
        to = monkey['test_out'][1]
      monkeys[to]['items'].append(nw)

    monkey['items'] = []

  if r == 20:
    break

  r += 1

# pp(monkeys)

ins = []
for monkey in monkeys:
  ins.append(monkey['inspects'])

ins.sort(reverse=True)

# pp(ins)

ans = ins[0] * ins[1]
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

monkeys = []

curr_monkey = {'inspects': 0}
for i, line in enumerate(plines):
  if not line:
    monkeys.append(curr_monkey)
    curr_monkey = {'inspects': 0}

  tokens = line.split(' ')

  if tokens[0] == 'Monkey':
    curr_monkey['id'] = int(tokens[1][:-1])
  elif tokens[0] == 'Starting':
    items = [int(t) for t in line.split(':')[1].split(',') if t]
    curr_monkey['items'] = items
  elif tokens[0] == 'Operation:':
    op = line.split('=')[1]
    op = op.replace('old', '{old}').strip()
    curr_monkey['op'] = op
  elif tokens[0] == 'Test:':
    val = int(tokens[-1])
    tests = []
    curr_monkey['test_in'] = val
  elif tokens[0] == 'If':
    val = int(tokens[-1])
    tests.append(val)
    curr_monkey['test_out'] = tests

r = 1

common = lcm(*[m['test_in'] for m in monkeys])

while True:
  for mid, monkey in enumerate(monkeys):
    if not monkey['items']:
      continue

    for item in monkey['items']:
      monkey['inspects'] += 1

      w = eval(monkey['op'].format(old=item))
      nw = (w % common) + common

      if nw % monkey['test_in'] == 0:
        to = monkey['test_out'][0]
      else:
        to = monkey['test_out'][1]
      monkeys[to]['items'].append(nw)

    monkey['items'] = []

  if r == 10000:
    break

  r += 1

# pp(monkeys)

ins = []
for monkey in monkeys:
  ins.append(monkey['inspects'])

ins.sort(reverse=True)

# pp(ins)

ans = ins[0] * ins[1]
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
