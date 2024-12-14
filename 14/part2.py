import time

start_time = time.time()

"""
by a lucky guess, you get a picture of a christmas
tree if no robots overlap in location

that's it
that's the whole thing
"""

def parse_file(filename):
    robots = []
    with open(filename) as infile:
        for line in infile.readlines():
            line = line.strip()
            p, v = line.split(' ')
            x, y = map(int, p.replace('p=', '').split(','))
            dx, dy = map(int, v.replace('v=', '').split(','))
            robots.append((x, y, dx, dy))

    return robots

WIDTH = 101
HEIGHT = 103
robots = parse_file("input.txt")

def step_robot(x, y, dx, dy):
    x += dx
    y += dy
    if x >= WIDTH:
        x -= WIDTH
    elif x < 0:
        x += WIDTH

    if y >= HEIGHT:
        y -= HEIGHT
    elif y < 0:
        y += HEIGHT
    return x, y, dx, dy

def check_uniquness():
    visited = set()

    for x, y, _, _ in robots:
        if (x, y) in visited:
            return False

        visited.add((x, y))

    return True

def find_easter_egg():
    # choose a suitably big number
    for i in range(100000000000):
        if check_uniquness():
            return i
        else:
            for i, (x, y, dx, dy) in enumerate(robots):
                robots[i] = step_robot(x, y, dx, dy)

print(f"steps to find easter egg: {find_easter_egg()}")  # 6475
print(f"took {time.time() - start_time}s")
