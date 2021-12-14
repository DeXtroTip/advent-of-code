# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 14

DEBUG = 'x' in sys.argv
# fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{} -> {}'
  tokens = parse.search(pattern, line).fixed

  return tokens


try:
  fin = aoc.get_input(DAY, example=DEBUG)
  ints = get_ints(fin)
except:
  pass
try:
  fin = aoc.get_input(DAY, example=DEBUG)
  lines = get_lines(fin, parse_pattern=None)
  TT = lines[0]
  lines = [parse_line(line) for line in lines[2:]]
except Exception as e:
  pass
try:
  fin = aoc.get_input(DAY, example=DEBUG)
  g = get_matrix(fin)
  g = get_matrix(fin, cast=int)
except:
  pass
finally:
  fin = aoc.get_input(DAY, example=DEBUG)

rules = {k: v for k, v in lines}

###


def p1():
  return


ans = 0

xx = TT
for _ in range(10):
  ns = ''
  for i in range(len(xx) - 1):
    q1, q2 = xx[i], xx[i + 1]
    r = rules.get(q1 + q2)
    ns += q1
    if r:
      ns += r
  ns += xx[-1]
  xx = ns

cc = Counter(xx)
ans = max(cc.values()) - min(cc.values())
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit p1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

###


def p2():
  return


ans = 0

xx = TT
cc = Counter(xx)

patterns = defaultdict(int)
for i in range(len(xx) - 1):
  patterns[xx[i:i + 2]] += 1

for _ in range(40):
  np = defaultdict(int)
  for ri, rf in rules.items():
    if patterns[ri] > 0:
      nn1 = ri[0] + rf
      nn2 = rf + ri[1]
      np[ri] -= patterns[ri]
      np[nn1] += patterns[ri]
      np[nn2] += patterns[ri]
      cc[rf] += patterns[ri]
  for p, v in np.items():
    patterns[p] += v
  for p in list(patterns.keys()):
    if patterns[p] < 1:
      del patterns[p]

ans = max(cc.values()) - min(cc.values())
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit p2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
