from snailfish_utils import add, full_reduce, get_magnitude, parse_snailfish_number

input = open("input.txt").read().splitlines()


out = parse_snailfish_number(input[0])
for i in range(1, len(input)):
    row = parse_snailfish_number(input[i])
    out = add(out, row)
    out = full_reduce(out)


print(get_magnitude(out))
