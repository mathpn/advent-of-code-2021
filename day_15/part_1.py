from dijkstra import shortest_distance

input = open("input.txt").read().splitlines()
risk_array = [list(map(int, row)) for row in input]

print(shortest_distance(risk_array))
