import re


input = open("input.txt").read()

x_0, x_1, y_0, y_1 = map(
    int, re.match("target area: x=([0-9]+)\.\.([0-9]+), y=-([0-9]+)..-([0-9]+)", input).groups()
)


def render_path(x_vel, y_vel):
    x = y = 0
    while True:
        x += x_vel
        y += y_vel
        x_vel = max(0, x_vel - 1)
        y_vel -= 1
        yield (x, y)


hits = 0
for x_vel in range(0, x_1 + 1):
    for y_vel in range(-y_0, y_0 + 1):
        hit_target = False
        for x, y in render_path(x_vel, y_vel):
            hit_target = hit_target or (x_0 <= x <= x_1 and -y_0 <= y <= -y_1)
            if x > x_1 or y < -y_0:
                break
        if hit_target:
            hits += 1

print(hits)
