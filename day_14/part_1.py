from collections import defaultdict

input = open("input.txt").read().splitlines()

polymer = input[0]

rules = {}
for row in input[2:]:
    a, b = row.split(" -> ")
    rules[a] = b

def expansion_step(polymer):
    prev = 0
    expanded_polymer = []
    for i in range(len(polymer)):
        if insertion := rules.get(polymer[i:i+2]):
            expanded_polymer.append(polymer[prev:i+1] + insertion + polymer[i+1])
            prev = i + 2
    return "".join(expanded_polymer)

for _ in range(10):
    polymer = expansion_step(polymer)

counts = defaultdict(int)
for letter in polymer:
    counts[letter] += 1

counts = sorted(counts.values(), reverse=True)
print(counts[0] - counts[-1])
