# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 4

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def parse_line(line):
  tokens = [t for t in line.split(' ')]
  return tokens


def win(board):
  cs = [p for n, p in board['b'].items() if n in board['ns']]
  if len(cs) < 5:
    return False
  xcounter = Counter([c[0] for c in cs])
  ycounter = Counter([c[1] for c in cs])
  if 5 in xcounter.values() or 5 in ycounter.values():
    return True
  # if (0, 0) in cs and (1, 1) in cs and (2, 2) in cs and (3, 3) in cs and (4, 4) in cs:
  #   return True
  # if (0, 4) in cs and (1, 3) in cs and (2, 2) in cs and (3, 1) in cs and (4, 0) in cs:
  #   return True
  return False


def part1():

  numbers = [int(n) for n in DATA_INPUT[0].split(',')]

  boards = []
  o = 0
  for i, line in enumerate(DATA_INPUT[1:]):
    if not line:
      boards.append({'b': {}, 'ns': set()})
      o = 0
      continue

    d = boards[-1]
    k = [int(n) for n in line.strip().split(' ') if n]
    for j, n in enumerate(k):
      d['b'][n] = (o, j)

    o += 1

  for r, bn in enumerate(numbers):
    for board in boards:
      if bn in board['b']:
        board['ns'].add(bn)
        if win(board):
          return sum(int(n) for n in board['b'].keys() if n not in board['ns']) * bn


def part2():

  numbers = [int(n) for n in DATA_INPUT[0].split(',')]

  boards = []
  o = 0
  for i, line in enumerate(DATA_INPUT[1:]):
    if not line:
      boards.append({'b': {}, 'ns': set()})
      o = 0
      continue

    d = boards[-1]
    k = [int(n) for n in line.strip().split(' ') if n]
    for j, n in enumerate(k):
      d['b'][n] = (o, j)

    o += 1

  finished = []
  for r, bn in enumerate(numbers):
    if len(finished) == len(boards):
      board = finished[-1]
      return sum(int(n) for n in board['b'].keys() if n not in board['ns']) * numbers[r - 1]

    for board in boards:
      if board in finished:
        continue
      if bn in board['b']:
        board['ns'].add(bn)
        if win(board):
          finished.append(board)


p1 = part1()
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2()
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
