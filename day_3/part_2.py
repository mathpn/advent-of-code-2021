from itertools import compress

input = open("./input.txt").read().splitlines()

def binary_to_decimal(binary):
    print(binary)
    decimal = 0
    for value in binary:
        decimal = decimal * 2 + int(value)
    return decimal

# find oxygen rate
oxy_input = input.copy()
for i in range(len(input[0])):
    common_bit = int(sum(int(row[i]) for row in oxy_input) / len(oxy_input) >= 0.5)
    keep = [int(row[i]) == common_bit for row in oxy_input]
    oxy_input = list(compress(oxy_input, keep))
    if len(oxy_input) == 1:
        oxygen_rate = binary_to_decimal(list(oxy_input[0]))
        break

# find co2 rate
co2_input = input.copy()
for i in range(len(input[0])):
    common_bit = int(sum(int(row[i]) for row in co2_input) / len(co2_input) >= 0.5)
    keep = [int(row[i]) != common_bit for row in co2_input]
    co2_input = list(compress(co2_input, keep))
    if len(co2_input) == 1:
        print(co2_input)
        co2_rate = binary_to_decimal(list(co2_input[0]))
        break

print(oxygen_rate)
print(co2_rate)
print(f"Life support rating: {oxygen_rate * co2_rate}")
