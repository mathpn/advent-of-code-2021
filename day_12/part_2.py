input = open("input.txt").read().splitlines()

connections = {}
for row in input:
    a, b = row.split("-")
    connections.setdefault(a, [])
    connections.setdefault(b, [])
    connections[a].append(b)
    connections[b].append(a)


def max_count(seq):
    unique = set(elem for elem in seq if elem.islower())
    return max(
        sum(elem == x for elem in seq)
        for x in unique
    )


def traverse_path(cave, connections, path, paths):
    path = path.copy()
    path.append(cave)
    for new_cave in connections[cave]:
        if new_cave == "start":
            continue
        if new_cave.islower() and new_cave in path and max_count(path) >= 2:
            continue
        if new_cave == "end":
            paths.append(path + ["end"])
        else:
            paths = traverse_path(new_cave, connections, path, paths)
    return paths

paths = traverse_path("start", connections, [], [])

# print("\n".join(",".join(path) for path in paths))
print(len(paths))
