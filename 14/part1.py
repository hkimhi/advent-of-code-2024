import time

EXAMPLE = False
start_time = time.time()

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

if EXAMPLE:
    WIDTH = 11
    HEIGHT = 7
    robots = parse_file("example.txt")
else:
    WIDTH = 101
    HEIGHT = 103
    robots = parse_file("input.txt")

def simulate(steps=100):
    quadrants = [0, 0, 0, 0]

    for _ in range(steps):
        for i, (x, y, dx, dy) in enumerate(robots):
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
            robots[i] = (x, y, dx, dy)

    for x, y, _, _ in robots:
        if x < WIDTH // 2 and y < HEIGHT // 2:
            # quadrant 1
            quadrants[0] += 1
        elif x > WIDTH // 2 and y < HEIGHT // 2:
            # quadrant 2
            quadrants[1] += 1
        elif x < WIDTH // 2 and y > HEIGHT // 2:
            # quadrant 3
            quadrants[2] += 1
        elif x > WIDTH // 2 and y > HEIGHT // 2:
            # quadrant 4
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

print(f"safety factor: {simulate()}")  # 231782040
print(f"took {time.time() - start_time}s")
