# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2022, 3

fin = aoc.get_input(DAY, example=True)
rucksacks = get_lines(fin)

common_items = []
for rucksack in rucksacks:
  common = next(iter(collections_intersect(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:])))
  common_items.append(common)
ans = sum(ord(item) - (96 if item.islower() else 38) for item in common_items)
aoc.print_answer(ans, 1)

common_items = []
for i in range(0, len(rucksacks), 3):
  common = next(iter(collections_intersect(*rucksacks[i:i + 3])))
  common_items.append(common)
ans = sum(ord(item) - (96 if item.islower() else 38) for item in common_items)
aoc.print_answer(ans, 2)
