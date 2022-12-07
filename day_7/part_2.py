from itertools import accumulate

input = list(map(int, open('./input.txt').read().split(',')))

max_coord = max(input)
costs = list(accumulate(range(max_coord + 1)))
print(
    min(
        (sum(costs[abs(pos - coord)] for pos in input) for coord in range(max_coord))
    )
)