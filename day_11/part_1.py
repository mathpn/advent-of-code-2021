input = open("./input.txt").read().splitlines()

array = [list(map(int, list(row))) for row in input]
n_rows = len(array)
n_cols = len(array[0])


def get_neighbors(x, y):
    coords = []
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            if a < 0 or b < 0:
                continue
            if a >= n_rows or b >= n_rows:
                continue
            coords.append((a, b))
    return coords


def increase_neighbors(array, row, col):
    neighbors = get_neighbors(row, col)
    for row, col in neighbors:
        if array[row][col] == 0:
            continue
        array[row][col] += 1
    return array


flashes = 0
for _ in range(100):
    for row in range(len(array)):
        for col in range(len(array[0])):
            array[row][col] += 1

    while True:
        if not any((count and count > 9) for row in array for count in row):
            break
        for row in range(len(array)):
            for col in range(len(array[0])):
                if array[row][col] > 9:
                    flashes += 1
                    array[row][col] = 0
                    array = increase_neighbors(array, row, col)

print(f"Number of flashes: {flashes}")