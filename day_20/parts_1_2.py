input = open("./input.txt").read().splitlines()

enhancing = [int(x == "#") for x in input[0]]

image = input[2:]
image = [[int(x == "#") for x in row] for row in image]


def binary_to_decimal(sequence):
    out = 0
    for digit in sequence:
        out = 2 * out + digit
    return out


def get_output_position(image, row, col, infinite_value):
    n_row = len(image)
    n_col = len(image[0])
    indices = [(a, b) for a in range(row - 1, row + 2) for b in range(col - 1, col + 2)]
    binary = []
    for row_idx, col_idx in indices:
        if row_idx < 0 or row_idx >= n_row:
            binary.append(infinite_value)
            continue
        if col_idx < 0 or col_idx >= n_col:
            binary.append(infinite_value)
            continue
        binary.append(image[row_idx][col_idx])
    position = binary_to_decimal(binary)
    return position


def enhance_image(image, infinite_value):
    new_image = [[0 for _ in range(len(image[0]) + 2)] for _ in range(len(image) + 2)]
    for row in range(-1, len(image) + 1):
        for col in range(-1, len(image[0]) + 1):
            position = get_output_position(image, row, col, infinite_value)
            value = enhancing[position]
            new_image[row + 1][col + 1] = value
    infinite_value = enhancing[binary_to_decimal([infinite_value for _ in range(9)])]
    return new_image, infinite_value


def print_image(image):
    for row in image:
        row = ["#" if x == 1 else "." for x in row]
        print("".join(row))


# part 1
infinite_value = 0
for _ in range(2):
    image, infinite_value = enhance_image(image, infinite_value)
print(sum(sum(row) for row in image))

# part 2
infinite_value = 0
for _ in range(48):
    image, infinite_value = enhance_image(image, infinite_value)
print(sum(sum(row) for row in image))
