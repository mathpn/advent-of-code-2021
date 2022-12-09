input = open('./input.txt').read().splitlines()

lines = [line.split("|")[1].strip() for line in input]

print(
    sum(
        len(signal) in (2, 4, 3, 7) for line in lines for signal in line.split(' ')
    )
)
