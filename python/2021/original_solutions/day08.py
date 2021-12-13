# flake8: noqa

import sys

from utils.all import *

YEAR = 2021
DAY = 8

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)

DATA_INPUT = get_lines(fin)


def parse_line(line):
  tokens = [t for t in line.split('|')]
  return tokens[0].strip().split(' '), tokens[1].strip().split(' ')


def signal_to_num(w, mapx):
  # [a, b, c, d, e, f, g] in dict way
  rx = tuple(sorted(mapx[x] for x in w))
  if rx == (0, 1, 2, 4, 5, 6):
    return 0
  if rx == (2, 5):
    return 1
  if rx == (0, 2, 3, 4, 6):
    return 2
  if rx == (0, 2, 3, 5, 6):
    return 3
  if rx == (1, 2, 3, 5):
    return 4
  if rx == (0, 1, 3, 5, 6):
    return 5
  if rx == (0, 1, 3, 4, 5, 6):
    return 6
  if rx == (0, 2, 5):
    return 7
  if rx == (0, 1, 2, 3, 4, 5, 6):
    return 8
  if rx == (0, 1, 2, 3, 5, 6):
    return 9
  return None


def num_to_poss(num):
  if num == 0:
    return (0, 1, 2, 4, 5, 6)
  if num == 1:
    return (2, 5)
  if num == 2:
    return (0, 2, 3, 4, 6)
  if num == 3:
    return (0, 2, 3, 5, 6)
  if num == 4:
    return (1, 2, 3, 5)
  if num == 5:
    return (0, 1, 3, 5, 6)
  if num == 6:
    return (0, 1, 3, 4, 5, 6)
  if num == 7:
    return (0, 2, 5)
  if num == 8:
    return (0, 1, 2, 3, 4, 5, 6)
  if num == 9:
    return (0, 1, 2, 3, 5, 6)
  return tuple()


def segments_to_nums(w):
  if len(w) == 2:
    return (1, )
  if len(w) == 3:
    return (7, )
  if len(w) == 4:
    return (4, )
  if len(w) == 5:
    return (2, 3, 5)
  if len(w) == 7:
    return (8, )
  if len(w) == 6:
    return (0, 6, 9)
  return tuple()


def part1(data_input):
  total = 0
  for i, line in enumerate(data_input):
    ins, outs = parse_line(line)
    for x in outs:
      n = segments_to_nums(x)
      if n[0] in (1, 4, 7, 8):
        total += 1

  return total


# def get_comb(ins):
#   comb = {}
#   w_pos = defaultdict(dict)
#   for i, t in enumerate(ins):
#     possible_num = segments_to_nums(t)
#     pp(t)
#     pp(possible_num)
#     nw_pos = defaultdict(dict)
#     for n in possible_num:
#       num_combs = num_to_poss(n)
#       for w in t:
#         if not w_pos[w]:
#           nw_pos[w] = {tuple(sorted(set(num_combs))): {n}}
#         else:
#           nww = dict()
#           for curr_w, seq in w_pos[w].items():
#             if n in seq:
#               nww[curr_w] = seq
#               continue
#             nnn = tuple(sorted(set(curr_w).intersection(num_combs)))
#             if nnn:
#               nww[nnn] = seq | {n}
#           nw_pos[w].update(nww)
#     for w in t:
#       w_pos[w] = nw_pos[w]

#     pp(w_pos)
#     print()

#     if i == 2:
#       break
#   pp(w_pos)


def default_dict():
  return {n: set('abcdefg') for n in range(7)}


def get_comb(ins):
  possibs = []
  for i, t in enumerate(ins):
    possible_num = segments_to_nums(t)

    new_possibs = []
    for n in possible_num:
      num_combs = num_to_poss(n)

      dd = default_dict()
      dd.update({n: set(t) for n in num_combs})

      if not possibs:
        new_possibs.append(dd)
      else:
        for poss in possibs:
          np = default_dict()

          for k, v in poss.items():
            if k in dd:
              np[k] = v.intersection(dd[k])
            else:
              np[k] = v

          for k, v in dd.items():
            np[k] = np[k].intersection(v)

          while True:
            mark_singles = dict()
            for k, v in np.items():
              if len(v) == 1:
                mark_singles[k] = next(iter(v))

            changes = False
            for k in np.keys():
              prev = len(np[k])
              np[k] = set(np[k]).difference({vv for kk, vv in mark_singles.items() if kk != k})
              if prev != len(np[k]):
                changes = True

            if not changes:
              break

          if np and all(np.values()):
            new_possibs.append(np)

    possibs = new_possibs

  dq = deque()
  for p in possibs:
    dq.append(p)

  while dq:
    p = dq.popleft()
    if all(len(v) == 1 for v in p.values()):
      return {k: next(iter(v)) for k, v in p.items()}

    for k, v in p.items():
      if len(v) > 1:
        for vv in v:
          np = {**p, k: {vv}}

          while True:
            mark_singles = dict()
            for k, v in np.items():
              if len(v) == 1:
                mark_singles[k] = next(iter(v))

            changes = False
            for k in np.keys():
              prev = len(np[k])
              np[k] = set(np[k]).difference({vv for kk, vv in mark_singles.items() if kk != k})
              if prev != len(np[k]):
                changes = True

            if not changes:
              break

          if np and all(np.values()):
            dq.append(np)
        break


def part2(data_input):
  total = 0
  for i, line in enumerate(data_input):
    ins, outs = parse_line(line)
    r = get_comb(ins + outs)
    comb = {v: k for k, v in r.items()}

    s = ''
    for t in outs:
      s += str(signal_to_num(t, comb))
    total += int(s)
  return total


p1 = part1(DATA_INPUT)
aoc.print_answer(p1, 1)
aoc.submit_answer(p1, 1, day=DAY, year=YEAR)

p2 = part2(DATA_INPUT)
aoc.print_answer(p2, 2)
aoc.submit_answer(p2, 2, day=DAY, year=YEAR)
