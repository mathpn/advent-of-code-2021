from functools import reduce

input = open("./input.txt").read().splitlines()

char_pairs = {
    '{': '}',
    '[': ']',
    '<': '>',
    '(': ')',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def get_error_score(line):
    expected = []
    for char in line:
        if char in char_pairs:
            expected.append(char_pairs[char])
            continue
        if char != expected.pop():
            return points[char]
    return 0

print(sum(get_error_score(line) for line in input))
