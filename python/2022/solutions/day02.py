from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 2

fin = aoc.get_input(DAY)

POINTS = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
PLAY_MAP = {
  ('A', 'X'): 'Z',
  ('A', 'Y'): 'X',
  ('A', 'Z'): 'Y',
  ('B', 'X'): 'X',
  ('B', 'Y'): 'Y',
  ('B', 'Z'): 'Z',
  ('C', 'X'): 'Y',
  ('C', 'Y'): 'Z',
  ('C', 'Z'): 'X',
}

rounds = [line.split(' ') for line in get_lines(fin)]

score_first = 0
score_second = 0
for p1, p2 in rounds:
  score_first += POINTS[p2]
  if POINTS[p1] == POINTS[p2]:
    score_first += 3
  elif POINTS[p2] - POINTS[p1] in (1, -2):
    score_first += 6

  score_second += (POINTS[p2] - 1) * 3
  score_second += POINTS[PLAY_MAP[(p1, p2)]]

aoc.print_answer(score_first, 1)
aoc.print_answer(score_second, 2)
