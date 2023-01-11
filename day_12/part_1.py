input = open("input.txt").read().splitlines()

connections = {}
for row in input:
    a, b = row.split("-")
    connections.setdefault(a, [])
    connections.setdefault(b, [])
    connections[a].append(b)
    connections[b].append(a)

def traverse_path(cave, connections, path, paths):
    path = path.copy()
    path.append(cave)
    for new_cave in connections[cave]:
        if new_cave.islower() and new_cave in path:
            continue
        if new_cave == "end":
            paths.append(path + ["end"])
        paths = traverse_path(new_cave, connections, path, paths)
    return paths

paths = traverse_path("start", connections, [], [])
print(len(paths))
