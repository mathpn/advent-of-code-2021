from collections import defaultdict

input = open("./input.txt").read()

counts = defaultdict(int)
for fish in input.split(","):
    counts[int(fish)] += 1

def decrease_counts(counts):
    new_counts = defaultdict(int)
    for state in counts:
        if state - 1 >= 0:
            new_counts[state - 1] += counts[state]
        else:
            new_counts[6] += counts[state]
            new_counts[8] += counts[state]
    return new_counts

# part 1
for day in range(80):
    counts = decrease_counts(counts)
print(sum(counts.values()))

# part 2
for day in range(256):
    counts = decrease_counts(counts)
print(sum(counts.values()))
