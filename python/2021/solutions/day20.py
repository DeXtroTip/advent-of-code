from collections import defaultdict

from utils import aoc
from utils.algorithms import bin_to_int, dgrid_neighbors8_values
from utils.helpers import get_dgrid

YEAR, DAY = 2021, 20

fin = aoc.get_input(DAY)
algorithm = [1 if c == '#' else 0 for c in fin.readline().strip()]
image = defaultdict(lambda: '.', get_dgrid(fin, cast=lambda c: 1 if c == '#' else 0))

min_x = int(min(image.keys(), key=lambda p: p[0])[0])
max_x = int(max(image.keys(), key=lambda p: p[0])[0])
min_y = int(min(image.keys(), key=lambda p: p[1])[1])
max_y = int(max(image.keys(), key=lambda p: p[1])[1])

pixel_toggle = algorithm[0] == 1
pixel_out = 0
for step in range(50):
  if step == 2:
    aoc.print_answer(sum(image.values()), 1)

  min_x -= 1
  max_x += 1
  min_y -= 1
  max_y += 1

  updated_image = defaultdict(int, image)
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      v8x = list(dgrid_neighbors8_values(image, (x, y), default=pixel_out))
      v8x.insert(4, image[(x, y)] if (x, y) in image else pixel_out)
      updated_image[(x, y)] = algorithm[bin_to_int(''.join(map(str, v8x)))]

  image = updated_image
  if pixel_toggle:
    pixel_out ^= 1

aoc.print_answer(sum(image.values()), 2)
