__all__ = [
  'get_ints',
  'get_lines',
]

import re


def get_ints(f):
  return list(map(int, f.readlines()))


def get_lines(f, regex=None, parse_pattern=None, strip=True):
  if parse_pattern is not None:
    import parse
    return [parse.search(parse_pattern, line.strip() if strip else line).fixed for line in f.readlines()]
  if regex is not None:
    return [re.compile(regex).findall(line.strip() if strip else line)[0] for line in f.readlines()]

  return [line.strip() if strip else line for line in f.readlines()]
