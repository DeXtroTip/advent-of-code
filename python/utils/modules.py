# flake8: noqa

import functools
import heapq
import itertools
import math
import re
import string
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from functools import lru_cache, partial, reduce
from importlib import find_loader
from itertools import (combinations, count, filterfalse, islice, permutations, product)
from pprint import pp

from .math_override import *

if find_loader('numpy') is not None:
  import numpy as np

if find_loader('networkx') is not None:
  import networkx as nx

if find_loader('parse') is not None:
  import parse

if find_loader('aocd') is not None:
  import aocd

if find_loader('z3') is not None:
  import z3
