input = open("./input.txt").read().splitlines()

def binary_to_decimal(binary):
    decimal = 0
    for value in binary:
        decimal = decimal * 2 + value
    return decimal

bit_count = [0] * len(input[0])

for row in input:
    for i, bit in enumerate(row):
        bit_count[i] += int(bit)

bit_count = [count / len(input) for count in bit_count]

gamma = [int(count >= 0.5) for count in bit_count]
epsilon = [1 - bit for bit in gamma]

print(f"Power consumption: {binary_to_decimal(gamma) * binary_to_decimal(epsilon)}")

