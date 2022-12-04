input = open("./input.txt").read().splitlines()

lines = []
max_x = 0
max_y = 0
for line in input:
    a, b = line.split(' -> ')
    x_range, y_range = zip(*(map(int, a.split(",")), map(int, b.split(","))))
    max_x = max(max_x, x_range[0], x_range[1])
    max_y = max(max_y, y_range[0], y_range[1])
    lines.append((x_range, y_range))

diagram = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]
for x_range, y_range in lines:
    if not (x_range[0] == x_range[1] or y_range[0] == y_range[1]):
        continue

    x_step = 1 if x_range[0] < x_range[1] else -1
    for x in range(x_range[0], x_range[1] + x_step, x_step):
        y_step = 1 if y_range[0] < y_range[1] else -1
        for y in range(y_range[0], y_range[1] + y_step, y_step):
            diagram[y][x] += 1

print(f"Overlap of at least two lines: {sum(x >= 2 for row in diagram for x in row)}")