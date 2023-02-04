from collections import defaultdict

input = open("input.txt").read().splitlines()

polymer = input[0]

rules = {}
for row in input[2:]:
    a, b = row.split(" -> ")
    rules[a] = b

polymer_pairs = defaultdict(int)
for i in range(len(polymer) - 1):
    polymer_pairs[polymer[i:i+2]] += 1


def expansion_step(polymer_pairs):
    prev_pairs = polymer_pairs.copy()
    for pair, count in prev_pairs.items():
        if count == 0:
            polymer_pairs.pop(pair)
        if added := rules.get(pair):
            polymer_pairs[pair] -= count
            polymer_pairs[pair[0] + added] += count
            polymer_pairs[added + pair[1]] += count
    return polymer_pairs


for _ in range(40):
    polymer_pairs = expansion_step(polymer_pairs)


counts = defaultdict(int)
for pair, count in polymer_pairs.items():
    a, b = list(pair)
    counts[a] += count
    counts[b] += count

counts = [count // 2 + count % 2 for count in counts.values()]
counts = sorted(counts, reverse=True)
print(counts[0] - counts[-1])
