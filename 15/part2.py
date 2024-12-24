"""
Let's talk a little about what's going on here, cause it's a mess

With part2, boxes become twice as wide. This has basically no effect
on horizontal movement ('>' or '<') because they're just treated as
multiple part1 boxes in sequence

This has a lot of significance for vertical movement ('^' or 'v')
though. The main issue is in detecting "collisions" or which boxes
are actually touching other boxes (since they can touch at a half-length).

The approach taken in this file (which is wrong, and i will explain below why)
is to continually widen the "search space" when trying to push up or down.

Say we're pushing down, and we have this initial setup

....
.@..
[]..
.[].
^ ^
| |
| |

to detect the "2-depth" box, I create an imaginary row (marked by the arrows)
and look for any boxes in that row. When I find a box touching another box, I
widen the row (if the box is cut in half at the row boundary)

The reason this doesn't work is illustrated with this example (with a ^ move)

[].[].[]
.[]..[].
..[][]..
...[]...
...@....

the box at the top middle should NOT be moved, but in the "row" method described
above, I would move it since I don't check for 'internal' collisions
"""

from pprint import pp
import time

start_time = time.time()

with open("example3.txt") as infile:
    original_map, directions = infile.read().split('\n\n')

# resize map
map = []
for row in original_map.split("\n"):
    new_row = ""
    for char in row:
        if char == '#':
            new_row += "##"
        elif char == 'O':
            new_row += "[]"
        elif char == '.':
            new_row += ".."
        elif char == '@':
            new_row += "@."
    map.append(list(new_row))

directions = directions.replace('\n', '')

robot_pos = None
for x, row in enumerate(map):
    for y, char in enumerate(row):
        if char == '@':
            robot_pos = (x, y)
            break
    if robot_pos is not None:
        break

def can_move(pos, dir):
    x, y = pos
    if not (0 <= x < len(map) and 0 <= y < len(map[0])):
        return False

    if dir == '^':
        if map[x - 1][y] == ']':
            left = y - 1
            right = y
        elif map[x - 1][y] == '[':
            left = y
            right = y + 1
        else:
            left = y
            right = y

        i = 1
        row = map[x - i][left:right]
        while not all(char == '.' for char in row):
            if any(char == '#' for char in row):
                # cannot move up
                i = 0
                break
            else:
                # have a box somewhere, have to check next row up
                i += 1
                row = map[x - i][left:right]
                if row[0] == ']':
                    left -= 1
                if row[-1] == '[':
                    right += 1
                row = map[x - i][left:right]

        new_pos = (x - i, y)
    elif dir == 'v':
        if map[x + 1][y] == ']':
            left = y - 1
            right = y
        elif map[x + 1][y] == '[':
            left = y
            right = y + 1
        else:
            left = y
            right = y

        i = 1
        row = map[x + i][left:right]
        while not all(char == '.' for char in row):
            if any(char == '#' for char in row):
                # cannot move up
                i = 0
                break
            else:
                # have a box somewhere, have to check next row up
                i += 1
                row = map[x + i][left:right]
                if row[0] == ']':
                    left -= 1
                if row[-1] == '[':
                    right += 1
                row = map[x + i][left:right]

        new_pos = (x + i, y)
    elif dir == '>':
        new_pos = (x, y + 1)
    elif dir == '<':
        new_pos = (x, y - 1)

    next_char = map[new_pos[0]][new_pos[1]]
    if next_char == '.':
        return 1
    elif next_char == '#' or next_char == '@':
        # basically '@' is special return value for '^' or 'v' that end in no move
        # it's just when we set new_pos == pos
        return -1
    else:
        val = can_move(new_pos, dir)
        return (-1 if val == -1 else 1 + val)

for dir in directions:
    move_length = can_move(robot_pos, dir)
    breakpoint()
    if move_length != -1:
        # Can move
        x, y = robot_pos
        if dir == '>':
            for i in range(move_length, 0, -1):
                map[x][y + i] = map[x][y + i - 1]
            map[x][y] = '.'
            robot_pos = x, y + 1
        elif dir == '<':
            for i in range(move_length, 0, -1):
                map[x][y - i] = map[x][y - i + 1]
            map[x][y] = '.'
            robot_pos = x, y - 1
        elif dir == 'v':
            for _ in range(move_length):
                left = y
                right = y
                if map[x + 1][y] == ']':
                    left -= 1
                elif map[x + 1][y] == '[':
                    right += 1
                for i in range(x, x + move_length + 1):
                    map[i][left:right + 1] = map[i - 1][left:right + 1]
                    map[i - 1][left:right + 1] = ['.'] * (right + 1 - left)
                robot_pos = (x + 1, y)
                x += 1
        elif dir == '^':
            for _ in range(move_length):
                left = y
                right = y
                if map[x - 1][y] == ']':
                    left -= 1
                elif map[x - 1][y] == '[':
                    right += 1
                for i in range(x, x - move_length - 1, -1):
                    map[i][left:right + 1] = map[i + 1][left:right + 1]
                    map[i + 1][left:right + 1] = ['.'] * (right + 1 - left)
                robot_pos = (x - 1, y)
                x -= 1

sum = 0
for x, row in enumerate(map):
    for y, char in enumerate(row):
        if char == 'O':
            # is a box, calculate score
            sum += 100 * x + y

print(f"total GPS score: {sum}")  # 1414416
print(f"took {time.time() - start_time}s")
