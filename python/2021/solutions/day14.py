from collections import Counter, defaultdict

from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2021, 14

fin = aoc.get_input(DAY)

initial_template = (fin.readline() + fin.readline()).strip()
rules = {k: v for k, v in get_lines(fin, regex=r'(\w{2}) -> (\w)')}

counter = Counter(initial_template)

patterns = defaultdict(int)
for i in range(len(initial_template) - 1):
  patterns[initial_template[i:i + 2]] += 1

for step in range(40):
  if step == 10:
    aoc.print_answer(max(counter.values()) - min(counter.values()), 1)

  patterns_update = defaultdict(int)
  for rule_pattern, element in rules.items():
    match = patterns[rule_pattern]
    if match:
      counter[element] += match
      patterns_update[rule_pattern] -= match
      patterns_update[rule_pattern[0] + element] += match
      patterns_update[element + rule_pattern[1]] += match

  for pattern, value in patterns_update.items():
    patterns[pattern] += value

aoc.print_answer(max(counter.values()) - min(counter.values()), 2)
