input = open('input.txt').read().splitlines()

dots = []
folds = []
for row in input:
    if not row:
        continue
    if row.startswith("fold"):
        folds.append(row.replace("fold along ", "").split("="))
    else:
        dots.append(list(map(int, row.split(","))))


def fold_axis(pos, fold):
    if pos > fold:
        return 2 * fold - pos
    return pos

def fold_paper(dots, fold):
    axis = fold[0]
    fold = int(fold[1])
    if axis == "y": # horizontal fold
        dots = [(x, fold_axis(y, fold)) for x, y in dots]
    else:
        dots = [(fold_axis(x, fold), y) for x, y in dots]
    return sorted(set(dots))


for fold in folds:
    dots = fold_paper(dots, fold)

max_y = max(dot[1] for dot in dots) + 1
max_x = max(dot[0] for dot in dots) + 1
dots_array = [["." for _ in range(max_x)] for _ in range(max_y)]
for dot in dots:
    dots_array[dot[1]][dot[0]] = "#"

print("\n".join("".join(row) for row in dots_array))