# flake8: noqa

import sys

from utils.all import *

YEAR = 2020
DAY = 4

DEBUG = 'x' in sys.argv
fin = aoc.get_input(DAY, example=DEBUG)


def parse_line(line):
  tokens = [t for t in line.split(',')]

  pattern = '{}-{}'
  # tokens = parse.search(parse_pattern, line).fixed

  return line


try:
  ints = get_ints(fin)
except:
  fin = aoc.get_input(DAY, example=DEBUG)
  try:
    lines = get_lines(fin, parse_pattern=None)
    lines = [parse_line(line) for line in lines]
  except:
    fin = aoc.get_input(DAY, example=DEBUG)

lines = lines + ['']

###

ans = 0

passports = []
p = {}
for line in lines:
  if not line:
    passports.append(p)
    p = {}
  else:
    for t in line.split(' '):
      k, v = t.split(':')
      p[k] = v

for p in passports:
  if 'cid' in p:
    del p['cid']

ans = sum(len(p) == 7 for p in passports)

ans = ans
aoc.print_answer(ans, 1)
aoc.submit_answer(ans, 1, DAY, YEAR)

###

ans = 0

passports = []
p = {}
for line in lines:
  if not line:
    passports.append(p)
    p = {}
  else:
    for t in line.split(' '):
      k, v = t.split(':')
      p[k] = v

for p in passports:
  if 'cid' in p:
    del p['cid']

  byr = p.get('byr')
  if byr is None:
    p['invalid'] = 'byr'
    continue
  elif len(byr) != 4 or not byr.isdigit() or not 1920 <= int(byr) <= 2002:
    p['invalid'] = 'byr'
    continue

  iyr = p.get('iyr')
  if iyr is None:
    p['invalid'] = 'iyr'
    continue
  elif len(iyr) != 4 or not iyr.isdigit() or not 2010 <= int(iyr) <= 2020:
    p['invalid'] = 'iyr'
    continue

  eyr = p.get('eyr')
  if eyr is None:
    p['invalid'] = 'eyr'
    continue
  elif len(eyr) != 4 or not eyr.isdigit() or not 2020 <= int(eyr) <= 2030:
    p['invalid'] = 'eyr'
    continue

  hgt = p.get('hgt')
  if hgt is None:
    p['invalid'] = 'hgt1'
    continue
  else:
    t1, t2 = hgt[:-2], hgt[-2:]
    if t2 == 'in':
      if not t1.isdigit() or not 59 <= int(t1) <= 76:
        p['invalid'] = 'hgt2'
        continue
    elif t2 == 'cm':
      if not t1.isdigit() or not (150 <= int(t1) <= 193):
        p['invalid'] = 'hgt3'
        continue
    else:
      p['invalid'] = 'hgt4'
      continue

  hcl = p.get('hcl')
  if hcl is None:
    p['invalid'] = 'hcl'
    continue
  elif len(hcl) != 7 or hcl[0] != '#' or any(x not in 'abcdef0123456789' for x in hcl[1:]):
    p['invalid'] = 'hcl'
    continue

  ecl = p.get('ecl')
  if ecl is None:
    p['invalid'] = 'ecl'
    continue
  elif ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
    p['invalid'] = 'ecl'
    continue

  pid = p.get('pid')
  if pid is None:
    p['invalid'] = 'pid'
    continue
  elif len(pid) != 9 or not pid.isdigit():
    p['invalid'] = 'pid'
    continue

ans = sum('invalid' not in p for p in passports)

ans = ans
aoc.print_answer(ans, 2)
aoc.submit_answer(ans, 2, DAY, YEAR)
