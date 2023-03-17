input = open("input.txt").read().splitlines()

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def bin_to_decimal(binary):
    binary = map(int, binary)
    out = 0
    for v in binary:
        out = 2 * out + v
    return out


def parse_packet(packet):
    version = bin_to_decimal(packet[:3])
    type_id = bin_to_decimal(packet[3:6])

    if type_id == 4:  # literal
        value, end = parse_literal(packet[6:])
        return version, end + 6
    else:
        len_type_id = packet[6]
        if len_type_id == "0":
            n_bits_subpacket = bin_to_decimal(packet[7:22])
            end = 0
            values = []
            while end < n_bits_subpacket:
                value, end_ = parse_packet(packet[22 + end :])
                end += end_
                values.append(value)
            return version + sum(values), 22 + end
        elif len_type_id == "1":
            n_subpackets = bin_to_decimal(packet[7:18])
            parsed = 0
            end = 0
            values = []
            while parsed < n_subpackets:
                value, end_ = parse_packet(packet[18 + end :])
                end += end_
                parsed += 1
                values.append(value)
            return version + sum(values), 18 + end


def parse_literal(binary):
    number = ""
    for i in range(0, len(binary), 5):
        number += binary[i + 1 : i + 5]
        if binary[i] == "0":
            return bin_to_decimal(number), i + 5


for line in input:
    line = "".join([hex_to_bin[char] for char in line])
    print(parse_packet(line)[0])
