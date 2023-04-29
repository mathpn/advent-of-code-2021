def parse_snailfish_number(raw):
    parsed = []
    depth = 0
    for char in raw:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char == ",":
            continue
        else:
            parsed.append((int(char), depth))
    return parsed


def split(number):
    return [number // 2, number // 2 + number % 2]


def add(sf_a, sf_b):
    sf_a = [(n, depth + 1) for n, depth in sf_a]
    sf_b = [(n, depth + 1) for n, depth in sf_b]
    return sf_a + sf_b


def reduce(snailfish_n):
    for i, (number, depth) in enumerate(snailfish_n):
        next_number, next_depth = snailfish_n[i + 1] if i + 1 != len(snailfish_n) else (None, -1)
        if depth == next_depth >= 5:
            if i > 0:
                left_n, left_depth = snailfish_n[i - 1]
                snailfish_n[i - 1] = (left_n + number, left_depth)
            if i + 2 != len(snailfish_n):
                right_n, right_depth = snailfish_n[i + 2]
                snailfish_n[i + 2] = (right_n + next_number, right_depth)
            snailfish_n = snailfish_n[:i] + [(0, depth - 1)] + snailfish_n[i + 2 :]
            return snailfish_n
    for i, (number, depth) in enumerate(snailfish_n):
        if number >= 10:
            left, right = split(number)
            snailfish_n = (
                snailfish_n[:i] + [(left, depth + 1), (right, depth + 1)] + snailfish_n[i + 1 :]
            )
            return snailfish_n
    return snailfish_n


def full_reduce(snailfish_n):
    while True:
        new = reduce(snailfish_n)
        if new == snailfish_n:
            return snailfish_n
        snailfish_n = new


def get_magnitude(snailfish_n):
    while len(snailfish_n) > 1:
        max_depth = max(elem[1] for elem in snailfish_n)
        for i, (number, depth) in enumerate(snailfish_n):
            if depth != max_depth:
                continue
            next_n, next_d = snailfish_n[i + 1] if i + 1 != len(snailfish_n) else (None, None)
            if next_d != depth:
                snailfish_n = snailfish_n[:i] + [(number, depth - 1)] + snailfish_n[i + 1 :]
            else:
                snailfish_n = (
                    snailfish_n[:i] + [(3 * number + 2 * next_n, depth - 1)] + snailfish_n[i + 2 :]
                )
            break
    return snailfish_n[0][0]
