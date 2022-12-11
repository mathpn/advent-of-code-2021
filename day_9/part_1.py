input = open("./input.txt").read().splitlines()
array = [list(map(int, list(x))) for x in input]

horizontal = []
for row in array:
    left = [a - b < 0 for a, b in zip(row, [10] + row)]
    right = [a - b < 0 for a, b in zip([10] + row, row + [10])][1:]
    both = [a & b for a, b in zip(left, right)]
    horizontal.append(both)

vertical = []
for col in zip(*array):
    col = list(col)
    up = [a - b < 0 for a, b in zip(col, [10] + col)]
    down = [a - b < 0 for a, b in zip([10] + col, col + [10])][1:]
    both = [a & b for a, b in zip(up, down)]
    vertical.append(both)

risk = 0
for i, (h, v) in enumerate(zip(horizontal, zip(*vertical))):
    for j in range(len(h)):
        if h[j] and v[j]:
            risk += 1 + array[i][j]

print(f"Sum of risk levels: {risk}")