input = open("./input.txt").read().splitlines()
array = [list(map(int, list(x))) for x in input]
basin_borders = []
for row in array:
    border = [a == 9 for a in row]
    basin_borders.append(border)


def get_neighbors(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def check_neighbors(row, col, basin):
    neighbors = get_neighbors(row, col)
    for neighbor in neighbors:
        if neighbor in basin:
            continue
        n_row, n_col = neighbor
        if n_row < 0 or n_row >= len(array) or n_col < 0 or n_col >= len(array[0]):
            continue
        if array[n_row][n_col] == 9:
            continue
        basin.add((n_row, n_col))
        check_neighbors(n_row, n_col, basin)
    return basin


basins = []
basin_points = set()
for row in range(len(array)):
    for col in range(len(array[0])):
        if (row, col) in basin_points:
            continue
        if array[row][col] == 9:
            continue

        basin = check_neighbors(row, col, set())
        basins.append(basin)
        basin_points.update(basin)

out = 1
for basin_size in sorted([len(basin) for basin in basins], reverse=True)[:3]:
    out *= basin_size
print(out)
