import math
import heapq


def get_neighbors(x, y):
    return [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]


def shortest_distance(risk_array):
    visited = set()
    queue = [(0, (0, 0))]
    dists = {(0, 0): 0}
    heapq.heapify(queue)

    node = (0, 0)
    end_node = (len(risk_array) - 1, len(risk_array[0]) - 1)
    while True:
        node_dist, node = heapq.heappop(queue)
        if node in visited:
            continue
        node_dist = dists.get(node, math.inf)
        neighbors = get_neighbors(*node)
        for n_x, n_y in neighbors:
            if n_x < 0 or n_y < 0:
                continue
            if n_x >= len(risk_array) or n_y >= len(risk_array[0]):
                continue
            n_value = risk_array[n_x][n_y]
            new_dist = min(dists.get((n_x, n_y), math.inf), node_dist + n_value)
            dists[(n_x, n_y)] = new_dist
            heapq.heappush(queue, (new_dist, (n_x, n_y)))
        if node == end_node:
            break
        visited.add(node)

    return dists[end_node]
