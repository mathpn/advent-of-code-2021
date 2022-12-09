from itertools import permutations

input = open('./input.txt').read().splitlines()
lines = []
for line in input:
    left, right = line.split("|")
    lines.append((left.strip().split(' '), right.strip().split(' ')))

"""
Index positions for each digit segment:
    0
   xxxx
5 x    x 1
  x 6  x
   xxxx
4 x    x 2
  x    x
   xxxx
    3
"""
digits_to_segments = {
    0: [0, 1, 2, 3, 4, 5],
    1: [1, 2],
    2: [0, 1, 6, 4, 3],
    3: [0, 1, 6, 2, 3],
    4: [5, 6, 1, 2],
    5: [0, 5, 6, 2, 3],
    6: [0, 5, 6, 2, 3, 4],
    7: [0, 1, 2],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 6, 5, 2, 3],
}

easy_digits = {2: 1, 4: 4, 3: 7, 7: 8}
hard_digits = {5: [2, 3, 5], 6: [0, 6, 9]}
permus_5, permus_6 = [
    list(map(list, permutations(v, len(v))))
    for v in hard_digits.values()
]


def get_possibilities(line):
    possibilities = []
    for permu_5 in permus_5:
        for permu_6 in permus_6:
            i, j = 0, 0
            permu = []
            for segments in line:
                if len(segments) == 5:
                    permu.append(permu_5[i])
                    i += 1
                    continue
                if len(segments) == 6:
                    permu.append(permu_6[j])
                    j += 1
                    continue
                permu.append(easy_digits[len(segments)])
            possibilities.append(permu)
    return possibilities


def get_digit_codes(line, possibilities):
    for possibility in possibilities:
        positions = [set('abcdefg') for _ in range(7)]
        for segments, possible_digit in zip(line, possibility):
            digit_segments = digits_to_segments[possible_digit]
            for pos in digit_segments:
                positions[pos] = positions[pos] & set(segments)
        # remove decided segments from other positions
        for pos in positions:
            if len(pos) == 1:
                for pos_ in positions:
                    if len(pos_) == 1:
                        continue
                    pos_ -= pos
        if all(len(pos) == 1 for pos in positions):
            break

    positions = [x.pop() for x in positions]
    digit_codes = {}
    for i in range(10):
        digit_segments = digits_to_segments[i]
        digit_code = frozenset(positions[x] for x in digit_segments)
        digit_codes[digit_code] = i
    return digit_codes


total = 0
for left, right in lines:
    possibilities = get_possibilities(left)
    digit_codes = get_digit_codes(left, possibilities)
    total += int("".join(map(str, [digit_codes[frozenset(code)] for code in right])))
print(total)
