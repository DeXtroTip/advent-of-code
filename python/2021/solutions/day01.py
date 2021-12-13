from utils import aoc
from utils.helpers import get_ints

YEAR, DAY = 2021, 1

fin = aoc.get_input(DAY)

numbers = get_ints(fin)

ans = sum(x < y for x, y in zip(numbers, numbers[1:]))
aoc.print_answer(ans, 1)

ans = sum(sum(numbers[i - 3:i]) < sum(numbers[i - 2:i + 1]) for i in range(3, len(numbers)))
aoc.print_answer(ans, 2)
