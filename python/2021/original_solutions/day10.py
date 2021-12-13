# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 10

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def match(s):
  return {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
  }.get(s)


def points(s):
  return {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
  }[s]


def parse_line(line):
  tokens = [t for t in line.split(' ')]
  return tokens


def part1(data_input):
  total = 0

  for i, line in enumerate(data_input):
    dq = deque()
    for c in line:
      if c in '[({<':
        dq.append(c)
      else:
        last = None
        if dq:
          last = dq.pop()
        if c != match(last):
          total += points(c)
          break

  return total


def part2(data_input):

  def points(s):
    return {
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4,
    }[s]

  scores = []

  for i, line in enumerate(data_input):
    dq = deque()
    flag = False
    for c in line:
      if c in '[({<':
        dq.append(c)
      else:
        last = None
        if dq:
          last = dq.pop()
        if c != match(last):
          flag = True
          break
    if not flag:
      ps = 0
      while dq:
        x = dq.pop()
        ps = (ps * 5) + points(match(x))
      scores.append(ps)

  scores.sort()
  if len(scores) % 2 == 0:
    return scores[len(scores) // 2 - 1]
  return scores[(len(scores) - 1) // 2]


p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
