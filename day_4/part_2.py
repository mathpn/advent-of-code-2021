input = open("input.txt").read().splitlines()

chosen_numbers = [int(x) for x in input.pop(0).split(",")]
input.pop(0)

boards = []
board = []
for line in input:
    if not line and board:
        boards.append(board)
        board = []
        continue
    board.append([int(x) for x in line.split(' ') if x])

if board:
    boards.append(board)

chosen = set()
winners = set()
for number in chosen_numbers:
    chosen.add(number)
    for j, board in enumerate(boards):
        columns = list(zip(*board))
        if any(set(row).issubset(chosen) for row in board) or any(set(col).issubset(chosen) for col in columns):
            winners.add(j)
        if len(winners) == len(boards):
            remaining = {number for row in board for number in row} - chosen
            print(sum(remaining) * number)
            print(f"loser board: {j}")
            exit()
