def element_sum(*args):
  return tuple(map(sum, zip(*args)))


def set_bit(value, bit):
  return value | (1 << bit)


def clear_bit(value, bit):
  return value & ~(1 << bit)
