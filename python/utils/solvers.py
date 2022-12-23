def z3_abs(x):
  import z3
  return z3.If(x < 0, -x, x)
