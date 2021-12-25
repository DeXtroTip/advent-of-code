# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 24

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def to_int(s):
  try:
    return int(s)
  except ValueError:
    return None


def parse_line(line):
  tokens = [t for t in line.split(' ')]

  pattern = '{}-{}'
  # tokens = parse.search(pattern, line).fixed

  # return tokens
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
    #plines = [int(n) for n in plines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  # g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass

fin = aoc.get_input(DAY, example=DEBUG)

### input handle

### part 1

solver = z3.Optimize()
digits = [z3.BitVec(f'd{i}', 64) for i in range(14)]

for d in digits:
  solver.add(1 <= d)
  solver.add(d <= 9)

dinp = iter(digits)

zero = z3.BitVecVal(0, 64)
one = z3.BitVecVal(1, 64)

regs = {r: zero for r in 'xyzw'}

for i, line in enumerate(plines):
  op = line[0]
  reg = line[1]

  if op == 'inp':
    regs[reg] = next(dinp)
    continue

  val = line[2] if len(line) > 2 else None
  val = regs[val] if val in regs else int(val)

  vx = z3.BitVec(f'v{i}', 64)

  if op == 'add':
    solver.add(vx == regs[reg] + val)
  elif op == 'mul':
    solver.add(vx == regs[reg] * val)
  elif op == 'mod':
    solver.add(vx == regs[reg] % val)
  elif op == 'div':
    solver.add(vx == regs[reg] / val)
  elif op == 'eql':
    solver.add(vx == z3.If(regs[reg] == val, one, zero))
  else:
    assert False

  regs[reg] = vx

solver.add(regs['z'] == 0)

solver.push()
solver.maximize(sum((10**i) * d for i, d in enumerate(digits[::-1])))
print(solver.check())
m = solver.model()

ans = ''.join(str(m[d]) for d in digits)

aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

solver.pop()
solver.push()
solver.minimize(sum((10**i) * d for i, d in enumerate(digits[::-1])))
solver.check()
m = solver.model()

ans = ''.join(str(m[d]) for d in digits)

aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
