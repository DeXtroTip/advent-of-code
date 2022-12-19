# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 19

DEBUG = 'x' in sys.argv or 'i' in sys.argv
if 'i' in sys.argv:
  aoc.write_example(DAY)
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  pattern = '{} {:d}: Each {} robot costs {:d} ore. Each {} robot costs {:d} ore. Each {} robot costs {:d} ore and {:d} clay. Each {} robot costs {:d} ore and {:d} obsidian.'
  tokens = parse.search(pattern, line).fixed
  return tokens


lines = get_lines(fin, strip=True, parse_pattern=None)
plines = [parse_line(line) for line in lines]

### setup

blueprints = {}
blueprints_l = []

for i, line in enumerate(plines):
  _, b, _, ore, _, clay, _, obs1, obs2, _, geo1, geo2 = line

  bp = {
    "ore": (ore, 0, 0, 0),
    "clay": (clay, 0, 0, 0),
    "obsidian": (obs1, obs2, 0, 0),
    "geode": (geo1, 0, geo2, 0),
  }

  blueprints_l.append(bp)
  blueprints[b] = bp

### part 1

from pulp import *


def solve(blueprint, target):
  costs = (
    blueprint["ore"],
    blueprint["clay"],
    blueprint["obsidian"],
    blueprint["geode"],
  )

  MINUTES = target

  prob = LpProblem("robots problem", LpMaximize)

  robots = [
    tuple(LpVariable(f'r{j}_d{i}', 0, None, LpInteger) for j in range(1,
                                                                      len(costs) + 1)) for i in range(MINUTES + 1)
  ]
  ores = [
    tuple(LpVariable(f'o{j}_d{i}', 0, None, LpInteger) for j in range(1,
                                                                      len(costs) + 1)) for i in range(MINUTES + 1)
  ]

  prob += ores[-1][-1]

  for i in range(len(costs)):
    if i == 0:
      prob.add(robots[0][i] == 1)
    else:
      prob.add(robots[0][i] == 0)
    prob.add(ores[0][i] == 0)

  for i in range(1, MINUTES + 1):
    rs = robots[i]
    rsprev = robots[i - 1]
    os = ores[i]
    osprev = ores[i - 1]

    for j, r in enumerate(rs):
      prob.add(r >= rsprev[j])
      for k, oprev in enumerate(osprev):
        if costs[j][k]:
          prob.add(r <= rsprev[j] + 1)

    prob.add(sum(rs) - sum(rsprev) <= 1)

    created = [0 for _ in range(len(costs))]
    created_costs = [0 for _ in range(len(costs))]
    for j, (curr, prev) in enumerate(zip(rs, rsprev)):
      for k, cost in enumerate(costs[j]):
        created_costs[k] += (curr - prev) * cost

    for c, o in zip(created_costs, osprev):
      prob.add(c <= o)

    for j, o in enumerate(os):
      prob.add(osprev[j] >= created_costs[j])
      prob.add(o == osprev[j] + rsprev[j] - created_costs[j])

  prob.solve()

  # The status of the solution is printed to the screen
  print("Status:", LpStatus[prob.status])

  # Each of the variables is printed with it's resolved optimum value
  # for v in prob.variables():
  #   print(v.name, "=", v.varValue)
  for i, (rs, os) in enumerate(zip(robots, ores)):
    pp(
      f"After minute {i}: Resources {','.join(str(int(o.varValue)) for o in os)}; robots {','.join(str(int(r.varValue)) for r in rs)}"
    )
    # print(i)
    # for j, (r, o) in enumerate(zip(rs, os)):
    #   print(f"{j}: r={r.varValue}, o={o.varValue}")
    # print()

  v = value(prob.objective)
  return int(value(prob.objective))


TARGET = 24

qualities = [solve(bp, TARGET) for bp in blueprints_l]
ans = sum(i * q for i, q in enumerate(qualities, 1))
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, is_debug=DEBUG)

### part 2

TARGET = 32

blueprints_l = blueprints_l[:3]

ans = math.prod(solve(bp, TARGET) for bp in blueprints_l)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, is_debug=DEBUG)
