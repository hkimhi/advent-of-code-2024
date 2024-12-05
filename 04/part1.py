# target word = XMAS
TARGET = "XMAS"
DIRECTIONS = [
    (1, 0),     # forward
    (-1, 0),    # backward
    (0, 1),     # up
    (0, -1),    # down
    (1, 1),     # up right diagonal
    (-1, 1),    # up left diagonal
    (1, -1),    # down right diagonal
    (-1, -1)    # down left diagonal
]

with open("input.txt") as infile:
    lines = infile.readlines()

# convert strings to lists for easy char access
lines = [list(line) for line in lines]

occurrences = 0

def check_direction(x, y, delta_x, delta_y):
    for i in range(len(TARGET)):
        # out of bounds
        if not (0 <= x < len(lines) and 0 <= y < len(lines[0])):
            return False

        # letter does not line up to TARGET
        if not (lines[x][y] == TARGET[i]):
            return False

        x += delta_x
        y += delta_y

    # if made it out of loop, we found a match
    return True

# iterate over all chars
for i in range(len(lines)):
    for j in range(len(lines[0])):
        for delta_x, delta_y in DIRECTIONS:
            if check_direction(i, j, delta_x, delta_y):
                occurrences += 1

print(f"Count: {occurrences}")  # 2633
