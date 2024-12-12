import time

start_time = time.time()

with open("example2.txt") as infile:
    garden = [list(line.strip()) for line in infile.readlines()]

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

areas = {}
perimeters = {}

# algorithm?
# start on first plot
# try in each direction, recurse while same plant
# if new plant, start new bfs?
def dfs(x, y, visited):
    if (x, y) in visited:
        return

    visited.add((x, y))

    curr_letter = garden[x][y]
    if curr_letter in areas:
        areas[curr_letter] += 1
    else:
        areas[curr_letter] = 1
    num_adjacent = 0

    for (dx, dy) in DIRECTIONS:
        if 0 <= x + dx < len(garden) and 0 <= y + dy < len(garden[0]):
            letter = garden[x + dx][y + dy]
            if curr_letter == letter:
                num_adjacent += 1

    curr_perimeter = 4 - num_adjacent
    if curr_letter not in perimeters:
        perimeters[curr_letter] = curr_perimeter
    else:
        perimeters[curr_letter] += curr_perimeter

    for (dx, dy) in DIRECTIONS:
        if 0 <= x + dx < len(garden) and 0 <= y + dy < len(garden[0]):
            dfs(x + dx, y + dy, visited)

dfs(0, 0, set())

price = 0
for letter in areas:
    price += areas[letter] * perimeters[letter]

breakpoint()

print(f"total price: {price}")
print(f"took {time.time() - start_time}s")
