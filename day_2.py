def traverse_path(commands: list[list[str]]) -> tuple[int, int]:
    """Traverse a list of [command, units] commands and return a tuple of [distance, depth]."""
    position = 0
    depth = 0
    aim = 0
    for command, units in commands:
        units = int(units)
        if command == "forward":
            position += units
            depth += units * aim
        elif command == "down":
            aim += units
        else:
            aim -= units
    return position, depth


if __name__ == "__main__":
    with open("day_2_input.txt", "r") as file:
        commands = file.read().splitlines()

    commands = [command.split(" ") for command in commands]
    distance, depth = traverse_path(commands)
    print(distance * depth)
