from collections import namedtuple

from utils import aoc
from utils.helpers import get_lines

YEAR, DAY = 2022, 7

DIR_MAX_SIZE = 100000
DISK_SPACE_TOTAL = 70000000
DISK_SPACE_TARGET = 30000000

Directory = namedtuple('Directory', ['name', 'dirs', 'files', 'parent', 'full_path'])
File = namedtuple('File', ['name', 'size'])

fin = aoc.get_input(DAY)
lines = get_lines(fin)

root = Directory('/', {}, [], None, '/')
curr_dir = root
dirs = {'/': root}

for line in lines:
  tokens = line.split(' ')
  if tokens[0] == '$':
    if tokens[1] == 'cd':
      dir_name = tokens[2]
      if dir_name == '..':
        curr_dir = curr_dir.parent
      elif dir_name == '/':
        curr_dir = root
      else:
        curr_dir = curr_dir.dirs[dir_name]
  elif tokens[0] == 'dir':
    dir_name = tokens[1]
    full_path = f'{curr_dir.full_path}{dir_name}/'
    sub_dir = Directory(dir_name, {}, [], curr_dir, full_path)
    curr_dir.dirs[dir_name] = sub_dir
    dirs[full_path] = sub_dir
  else:
    size = int(tokens[0])
    file_name = tokens[1]
    curr_dir.files.append(File(file_name, size))

directory_sizes = {}


def calc_directory_size(d: Directory):
  size = 0
  for f in d.files:
    size += f.size
  for sub_d in d.dirs.values():
    size += calc_directory_size(sub_d)
  directory_sizes[d.full_path] = size
  return size


root_size = calc_directory_size(root)

ans = sum(size for size in directory_sizes.values() if size <= DIR_MAX_SIZE)
aoc.submit_handler(ans, part=1, day=DAY, year=YEAR, skip_confirmation=True)

missing = DISK_SPACE_TARGET - (DISK_SPACE_TOTAL - root_size)
ans = min(size for size in directory_sizes.values() if size >= missing)
aoc.submit_handler(ans, part=2, day=DAY, year=YEAR, skip_confirmation=True)
