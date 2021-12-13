from utils.aoc import get_input, print_answer
from utils.helpers import get_ints

fin = get_ints(get_input(1))

ans = sum(x < y for x, y in zip(fin, fin[1:]))
print_answer(ans, 1)

ans = sum(sum(fin[i - 3:i]) < sum(fin[i - 2:i + 1]) for i in range(3, len(fin)))
print_answer(ans, 2)
