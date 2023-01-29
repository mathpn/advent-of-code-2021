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


print(len(fold_paper(dots, folds[0])))
