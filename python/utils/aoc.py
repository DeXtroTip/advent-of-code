__all__ = [
  'submit_answer',
  'print_answer',
  'get_input',
]

import os

from .timer import timer

INPUTS_DIR = '../inputs'


def submit_answer(ans, part, day=None, year=None):
  from aocd import submit
  submit(ans, part=part, day=day, year=year)


def get_input(day, example=False, fname=None, start_timer=True):
  if fname is None:
    fname = f'{day:02d}{".example" if example else ""}.txt'
  fname = os.path.join(INPUTS_DIR, fname)
  f = open(fname, 'r')
  if start_timer:
    timer.start()
  return f


def print_answer(ans, part, get_timer=True):
  timer_str = f"(Took: {timer.lap():05f} s)   " if get_timer else ""
  print(f"{timer_str}Part {part}: {ans}")
