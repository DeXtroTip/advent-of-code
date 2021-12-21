from collections import Counter
from functools import lru_cache
from itertools import product

from utils import aoc
from utils.helpers import MAX_CACHE_SIZE, get_lines

YEAR, DAY = 2021, 21

fin = aoc.get_input(DAY)
lines = get_lines(fin, regex=r"Player \d starting position: (\d)")

start_pos = tuple(map(int, lines))

scores = [0, 0]
pos = list(start_pos)
rolled = 0
player = 0
while scores[0] < 1000 and scores[1] < 1000:
  pos[player] = (pos[player] + rolled * 3 + 6) % 10
  if not pos[player]:
    pos[player] = 10
  scores[player] += pos[player]

  rolled += 3
  player ^= 1

aoc.print_answer(min(scores) * rolled, 1)

ROLLSET = Counter(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))


@lru_cache(maxsize=MAX_CACHE_SIZE)
def play(scores, pos, player):
  if scores[0] >= 21:
    return 1, 0
  if scores[1] >= 21:
    return 0, 1

  w1, w2 = 0, 0
  for r, c in ROLLSET.items():
    npos = list(pos)
    nscores = list(scores)

    npos[player] = (npos[player] + r) % 10
    if not npos[player]:
      npos[player] = 10
    nscores[player] += npos[player]

    tw1, tw2 = play(tuple(nscores), tuple(npos), player ^ 1)
    w1 += tw1 * c
    w2 += tw2 * c

  return w1, w2


wins = play((0, 0), start_pos, 0)
aoc.print_answer(max(wins), 2)
