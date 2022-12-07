input = list(map(int, open('./input.txt').read().split(',')))

max_coord = max(input)
print(
    min(
        (sum([abs(pos - coord) for pos in input]) for coord in range(max_coord))
    )
)