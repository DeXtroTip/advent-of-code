import math
from collections import deque

from utils import aoc
from utils.algorithms import bin_to_int, hex_to_bin
from utils.helpers import get_lines

YEAR, DAY = 2021, 16

EVAL_METHOD = {
  0: sum,
  1: math.prod,
  2: min,
  3: max,
  5: lambda p: p[0] > p[1],
  6: lambda p: p[0] < p[1],
  7: lambda p: p[0] == p[1],
}


def packets_eval(type_id, sub_packets):
  return EVAL_METHOD[type_id]([val for _, _, val in sub_packets])


def process_packet(msg):
  version = bin_to_int(msg[:3])
  type_id = bin_to_int(msg[3:6])

  if type_id == 4:
    s = ''
    for i in range(6, len(msg), 5):
      s += msg[i + 1:i + 5]
      if msg[i] == '0':
        break
    bits = i + 5
    return (version, (), bin_to_int(s)), bits

  else:
    len_type_id = bin_to_int(msg[6])
    packets = []
    if len_type_id == 0:
      total_bits = bin_to_int(msg[7:22])
      next_bit = 22
      while next_bit - 22 < total_bits:
        sub_packet, bits = process_packet(msg[next_bit:])
        packets.append(sub_packet)
        next_bit += bits
    else:
      num_packets = bin_to_int(msg[7:18])
      next_bit = 18
      for _ in range(num_packets):
        sub_packet, bits = process_packet(msg[next_bit:])
        packets.append(sub_packet)
        next_bit += bits
    return (version, packets, packets_eval(type_id, packets)), next_bit


fin = aoc.get_input(DAY)
lines = get_lines(fin)
bin_message = ''.join(hex_to_bin(c) for c in lines[0])

root_packet, _ = process_packet(bin_message)

versions_total = 0

dq = deque((root_packet, ))
while dq:
  version, sub_packets, _ = dq.popleft()
  versions_total += version
  dq.extend(sub_packets)

aoc.print_answer(versions_total, 1)
aoc.print_answer(root_packet[2], 2)
