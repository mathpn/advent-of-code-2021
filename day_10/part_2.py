from functools import reduce

input = open("./input.txt").read().splitlines()

char_pairs = {
    '{': '}',
    '[': ']',
    '<': '>',
    '(': ')',
}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def get_line_completion(line):
    expected = []
    for char in line:
        if char in char_pairs:
            expected.append(char_pairs[char])
            continue
        if char != expected.pop():
            return None
    return expected[::-1]


def get_score(completion):
    out = 0
    for char in completion:
        out = 5 * out + points[char]
    return out

scores = sorted(
    map(
        get_score,
        filter(
            lambda x: x is not None,
            map(get_line_completion, input)
        )
    )
)
print(scores[len(scores) // 2])
