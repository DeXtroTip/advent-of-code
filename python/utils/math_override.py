__all__ = ['gcd', 'lcm']

import sys


def _gcd2(a, b):
  while b:
    a, b = b, a % b
  return a


def _gcd(*values):
  it = iter(values)
  res = next(it)
  for val in it:
    res = _gcd2(val, res)
  return res


def _lcm(*values):
  it = iter(values)
  res = next(it)
  for val in it:
    res = res * val // _gcd2(res, val)
  return res


if sys.version_info >= (3, 9):
  from math import gcd, lcm
else:
  gcd = _gcd
  lcm = _lcm
