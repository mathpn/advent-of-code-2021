from itertools import combinations

from snailfish_utils import add, full_reduce, get_magnitude, parse_snailfish_number

input = open("input.txt").read().splitlines()


out = parse_snailfish_number(input[0])
numbers = [parse_snailfish_number(row) for row in input]
pairs = combinations(numbers, 2)

max_magnitude = 0
for a, b in pairs:
    out = add(a, b)
    out = full_reduce(out)
    max_magnitude = max(get_magnitude(out), max_magnitude)

print(max_magnitude)
