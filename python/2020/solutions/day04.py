from utils import aoc
from utils.helpers import get_lines

YEAR = 2020
DAY = 4

fin = aoc.get_input(DAY)
lines = get_lines(fin) + ['']

required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

passports = []
curr = {}
for line in lines:
  if not line:
    passports.append(curr)
    curr = {}
  else:
    for key_value in line.split(' '):
      key, value = key_value.split(':')
      curr[key] = value

valid_passports = [passport for passport in passports if set(passport.keys()).issuperset(required_fields)]
aoc.print_answer(len(valid_passports), 1)

new_valid_count = len(valid_passports)
for passport in valid_passports:
  invalid = False
  for field_key, field_value in passport.items():
    if invalid:
      break

    if field_key == 'byr':
      if len(field_value) != 4 or not field_value.isdigit() or not 1920 <= int(field_value) <= 2002:
        invalid = True
    elif field_key == 'iyr':
      if len(field_value) != 4 or not field_value.isdigit() or not 2010 <= int(field_value) <= 2020:
        invalid = True
    elif field_key == 'eyr':
      if len(field_value) != 4 or not field_value.isdigit() or not 2020 <= int(field_value) <= 2030:
        invalid = True
    elif field_key == 'hgt':
      number, ltype = field_value[:-2], field_value[-2:]
      if ltype not in ('cm', 'in'):
        invalid = True
      elif ltype == 'cm' and (not number.isdigit() or not (150 <= int(number) <= 193)):
        invalid = True
      elif ltype == 'in' and (not number.isdigit() or not (59 <= int(number) <= 76)):
        invalid = True
    elif field_key == 'hcl':
      if len(field_value) != 7 or field_value[0] != '#' or any(x not in 'abcdef0123456789' for x in field_value[1:]):
        invalid = True
    elif field_key == 'ecl':
      if field_value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        invalid = True
    elif field_key == 'pid':
      if len(field_value) != 9 or not field_value.isdigit():
        invalid = True
  if invalid:
    new_valid_count -= 1

aoc.print_answer(new_valid_count, 2)
