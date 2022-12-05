# WIP: still need to clean this up a little better

from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 5


def parse_line(line):
  line = line[:-1]
  if not line:
    return None

  if '[' in line:
    return [(col, crate) for col, crate in enumerate(line[1::4], 1) if crate.strip()]

  if not line.startswith('move'):
    return int(line.strip().split(' ')[-1])

  return (int(n) for n in line.split(' ') if n.isdigit())


fin = aoc.get_input(DAY)
lines = [parse_line(line) for line in get_lines(fin, strip=False)]

num_stacks = next(iter(n for n in lines if isinstance(n, int)))
stacks_single = [[] for n in range(num_stacks)]
stacks_multi = [[] for n in range(num_stacks)]

is_moving_step = False
for line in lines:
  if isinstance(line, int):
    continue

  if line is None:
    is_moving_step = True
    continue

  if not is_moving_step:
    for stack, crate in line:
      stacks_single[stack - 1].append(crate)
      stacks_multi[stack - 1].append(crate)
  else:
    num_crates, start_stack, end_stack = line
    start_stack -= 1
    end_stack -= 1

    for stacks in (stacks_single, stacks_multi):
      crates = stacks[start_stack][:num_crates]
      if stacks is stacks_single:
        crates.reverse()
      stacks[end_stack] = crates + stacks[end_stack]
      stacks[start_stack] = stacks[start_stack][num_crates:]

ans = ''.join(stack[0] for stack in stacks_single)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

ans = ''.join(stack[0] for stack in stacks_multi)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
