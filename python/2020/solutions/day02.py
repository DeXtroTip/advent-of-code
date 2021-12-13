from collections import Counter

from utils import aoc
from utils.helpers import get_lines

YEAR = 2020
DAY = 2

fin = aoc.get_input(DAY)
lines = get_lines(fin, r"(\d+)-(\d+) (\w): (\w+)")

lines = [(int(line[0]), int(line[1]), line[2], line[3]) for line in lines]

valid = 0
for line in lines:
  char_min, char_max, char, word = line
  counter = Counter(word)
  if char_min <= counter[char] <= char_max:
    valid += 1

aoc.print_answer(valid, 1)

valid = 0
for line in lines:
  idx1, idx2, char, word = line
  if sum(word[idx - 1] == char for idx in (idx1, idx2)) == 1:
    valid += 1

aoc.print_answer(valid, 2)
