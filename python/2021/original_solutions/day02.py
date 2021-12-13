# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 2

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def parse_line(line):
  tokens = [t for t in line.split(' ')]
  return tokens[0], int(tokens[1])


def part1():
  hor = 0
  dep = 0

  for i, line in enumerate(DATA_INPUT):
    m, n = parse_line(line)

    if m == 'forward':
      hor += n
    elif m == 'down':
      dep += n
    elif m == 'up':
      dep -= n

  return hor * dep


def part2():
  hor = 0
  dep = 0
  aim = 0

  for i, line in enumerate(DATA_INPUT):
    m, n = parse_line(line)

    if m == 'forward':
      hor += n
      dep += (aim * n)
    elif m == 'down':
      aim += n
    elif m == 'up':
      aim -= n

  return hor * dep


p1 = part1()
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2()
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
