__all__ = [
  'submit_answer',
  'print_answer',
  'get_input',
  'write_example',
]

import os
import sys

from .timer import timer

INPUTS_DIR = '../inputs'


def submit_answer(ans, part, day=None, year=None):
  from aocd import submit
  submit(ans, part=part, day=day, year=year)


def get_input(day, example=False, fname=None, start_timer=True):
  fname = fname or f'{day:02d}{".example" if example else ""}.txt'
  fname = os.path.join(INPUTS_DIR, fname)
  f = open(fname, 'r')
  if start_timer:
    timer.start()
  return f


def write_example(day, fname=None):
  fname = fname or f'{day:02d}.example.txt'
  fname = os.path.join(INPUTS_DIR, fname)
  with open(fname, 'w') as f:
    # Stop read on linux: Ctrl+D; Ctrl+D
    f.write(sys.stdin.read())


def print_answer(ans, part, get_timer=True):
  timer_str = f"(Took: {timer.lap():05f} s)   " if get_timer else ""
  print(f"{timer_str}Part {part}: {ans}")  # noqa: T201
