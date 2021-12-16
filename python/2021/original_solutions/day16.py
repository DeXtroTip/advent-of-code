# flake8: noqa

import sys

from utils.all import *

YEAR, DAY = 2021, 16

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  # return tokens
  return line


try:
  fin = aoc.get_input(DAY, example=DEBUG)
  ints = get_ints(fin)
except:
  pass

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  lines = get_lines(fin, strip=True, parse_pattern=None)
except:
  lines = None
finally:
  if lines is not None:
    plines = [parse_line(line) for line in lines]

try:
  fin = aoc.get_input(DAY, example=DEBUG)
  dg = get_dgrid(fin, cast=None, y_start_at_top=True, strip=True)
  g = graph_from_dgrid(dg, weighted=True, neighbors=dgrid_neighbors4)
except:
  pass


def to_int(x):
  return int(x, 2)


def to_bin(x, fill=4):
  return bin(int(x, 16))[2:].zfill(fill)


inp = lines[0]

fin = aoc.get_input(DAY, example=DEBUG)

###

binp = [to_bin(x) for x in inp]
slabel = ''.join(binp)


def process_packet(label):
  pver = to_int(label[:3])
  tid = to_int(label[3:6])
  versions = [pver]
  if tid == 4:
    s = ''
    for i in range(6, len(label), 5):
      s += label[i + 1:i + 5]
      if label[i] == '0':
        break
    consumed = i + 5
    return [to_int(s)], consumed, versions
  else:
    ltid = to_int(label[6])
    sub_packets = []
    if ltid == 0:
      leng = to_int(label[7:22])
      next_idx = 22
      while leng > 0:
        sub, consumed, sub_versions = process_packet(label[next_idx:])
        versions += sub_versions
        leng -= consumed
        next_idx += consumed
        if isinstance(sub, list):
          sub_packets += sub
        else:
          sub_packets.append(sub)
    elif ltid == 1:
      ns = to_int(label[7:18])
      next_idx = 18
      for _ in range(ns):
        sub, consumed, sub_versions = process_packet(label[next_idx:])
        versions += sub_versions
        next_idx += consumed
        if isinstance(sub, list):
          sub_packets += sub
        else:
          sub_packets.append(sub)
    return sub_packets, next_idx, versions


packets, _, versions = process_packet(slabel)

vv = sum(versions)

#
ans = vv
aoc.print_answer(ans, 1)
if not DEBUG:
  input("Submit part 1 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 1, DAY, YEAR)

###


def process_packet2(label):
  pver = to_int(label[:3])
  tid = to_int(label[3:6])
  versions = [pver]
  if tid == 4:
    s = ''
    for i in range(6, len(label), 5):
      s += label[i + 1:i + 5]
      if label[i] == '0':
        break
    consumed = i + 5
    return to_int(s), consumed, versions
  else:
    ltid = to_int(label[6])
    sub_packets = []
    val = 0
    if ltid == 0:
      leng = to_int(label[7:22])
      next_idx = 22
      while leng > 0:
        sub, consumed, sub_versions = process_packet2(label[next_idx:])
        versions += sub_versions
        leng -= consumed
        next_idx += consumed
        if isinstance(sub, list):
          sub_packets += sub
        else:
          sub_packets.append(sub)
    elif ltid == 1:
      ns = to_int(label[7:18])
      next_idx = 18
      for _ in range(ns):
        sub, consumed, sub_versions = process_packet2(label[next_idx:])
        versions += sub_versions
        next_idx += consumed
        if isinstance(sub, list):
          sub_packets += sub
        else:
          sub_packets.append(sub)

    if tid == 0:
      val = sum(sub_packets)
    elif tid == 1:
      val = math.prod(sub_packets)
    elif tid == 2:
      val = min(sub_packets)
    elif tid == 3:
      val = max(sub_packets)
    elif tid == 5:
      val = int(sub_packets[0] > sub_packets[1])
    elif tid == 6:
      val = int(sub_packets[0] < sub_packets[1])
    elif tid == 7:
      val = int(sub_packets[0] == sub_packets[1])

    return val, next_idx, versions


val, _, _ = process_packet2(slabel)

ans = val
aoc.print_answer(ans, 2)
if not DEBUG:
  input("Submit part 2 ? (Ctrl-c to cancel)")
  aoc.submit_answer(ans, 2, DAY, YEAR)
