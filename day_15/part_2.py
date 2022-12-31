from dijkstra import shortest_distance

input = open("input.txt").read().splitlines()
tile_risk_array = [list(map(int, row)) for row in input]
dim = len(tile_risk_array)
assert dim == len(tile_risk_array[0])  # square map

full_map = [[0 for _ in range(5 * dim)] for _ in range(5 * dim)]
for i, x in enumerate(full_map):
    for j, y in enumerate(x):
        initial_value = tile_risk_array[i % dim][j % dim]
        full_map[i][j] = (initial_value + i // dim + j // dim - 1) % 9 + 1

print(shortest_distance(full_map))
