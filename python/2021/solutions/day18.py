import math
from itertools import product

from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2021, 18


class BinaryTree:

  @classmethod
  def from_list(cls, lst):
    if isinstance(lst, int):
      tree = cls(lst)
    else:
      tree = cls(None, None, cls.from_list(lst[0]), cls.from_list((lst[1])))
    return tree

  def __init__(self, data=None, parent=None, left=None, right=None):
    self.data = data
    self.parent = parent
    self.left = left
    self.right = right

    if self.left:
      self.left.parent = self
    if self.right:
      self.right.parent = self

  @property
  def value(self):
    if self.left is None and self.right is None:
      return self.data
    return self.left.value * 3 + self.right.value * 2

  def get_bottom_nodes(self, level=1):
    if self.left is None and self.right is None:
      return [(self, level - 1)]
    nodes = []
    if self.left:
      nodes += self.left.get_bottom_nodes(level + 1)
    if self.right:
      nodes += self.right.get_bottom_nodes(level + 1)
    return nodes

  def as_list(self):
    if self.left is None and self.right is None:
      return self.data
    nodes = []
    if self.left:
      nodes.append(self.left.as_list())
    if self.right:
      nodes.append(self.right.as_list())
    return nodes

  def reduce_(self):
    changes = True
    while changes:
      changes = False
      bottom_nodes = self.get_bottom_nodes()

      for i, p1 in enumerate(bottom_nodes[:-1]):
        n1, l1 = p1
        n2, l2 = bottom_nodes[i + 1]

        if n1.parent == n2.parent and l1 == 5:
          if i > 0:
            bottom_nodes[i - 1][0].data += n1.data
          if i + 2 < len(bottom_nodes):
            bottom_nodes[i + 2][0].data += n2.data
          n1.parent.data = 0
          n1.parent.left, n1.parent.right = None, None

          changes = True
          break

      if not changes:
        for p in bottom_nodes:
          node = p[0]
          if node.data > 9:
            node.left = BinaryTree(node.data // 2, node)
            node.right = BinaryTree(node.data // 2 if node.data % 2 == 0 else (node.data // 2) + 1, node)
            node.data = None
            changes = True
            break


fin = aoc.get_input(DAY)
lines = [eval(line) for line in get_lines(fin)]

trees = [BinaryTree.from_list(line) for line in lines]
curr = trees[0]
for tree in trees[1:]:
  curr = BinaryTree(None, None, curr, tree)
  curr.reduce_()

aoc.print_answer(curr.value, 1)

largest = -math.inf
for nums_combination in product(lines, lines):
  if nums_combination[0] == nums_combination[1]:
    continue
  for nums1, nums2 in zip(nums_combination, nums_combination[::-1]):
    join_tree = BinaryTree(None, None, BinaryTree.from_list(nums1), BinaryTree.from_list(nums2))
    join_tree.reduce_()
    largest = max(largest, join_tree.value)

aoc.print_answer(largest, 2)
