# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 3

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def part1():
  gamma = ''
  eps = ''
  for i in range(len(DATA_INPUT[0])):
    c0 = 0
    c1 = 0
    for w in DATA_INPUT:
      if w[i] == '0':
        c0 += 1
      else:
        c1 += 1
    if c1 > c0:
      gamma += '1'
      eps += '0'
    else:
      gamma += '0'
      eps += '1'
  gg = int(gamma, 2)
  ee = int(eps, 2)

  return gg * ee


def calc(is_ox):
  www = DATA_INPUT[::]
  for i in range(len(DATA_INPUT[0])):
    c0 = 0
    c1 = 0
    for w in www:
      if w[i] == '0':
        c0 += 1
      else:
        c1 += 1

    kk = None
    if is_ox:
      if c1 >= c0:
        kk = '1'
      else:
        kk = '0'
    else:
      if c1 >= c0:
        kk = '0'
      else:
        kk = '1'

    www = [j for j in www if j[i] == kk]
    if len(www) == 1:
      return int(www[0], 2)


def part2():
  return calc(True) * calc(False)


p1 = part1()
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2()
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
