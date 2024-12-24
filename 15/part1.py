import time

start_time = time.time()

with open("input.txt") as infile:
    map, directions = infile.read().split('\n\n')

map = [list(_) for _ in map.split("\n")]
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
        new_pos = (x - 1, y)
    elif dir == 'v':
        new_pos = (x + 1, y)
    elif dir == '>':
        new_pos = (x, y + 1)
    elif dir == '<':
        new_pos = (x, y - 1)

    next_char = map[new_pos[0]][new_pos[1]]
    if next_char == '.':
        return 1
    elif next_char == '#':
        return -1
    else:
        val = can_move(new_pos, dir)
        return (-1 if val == -1 else 1 + val)

for dir in directions:
    move_length = can_move(robot_pos, dir)
    if move_length != -1:
        # can move
        x, y = robot_pos
        for i in range(move_length, 0, -1):
            if dir == '>':
                map[x][y + i] = map[x][y + i - 1]
                robot_pos = x, y + 1
            elif dir == '<':
                map[x][y - i] = map[x][y - i + 1]
                robot_pos = x, y - 1
            elif dir == 'v':
                map[x + i][y] = map[x + i - 1][y]
                robot_pos = x + 1, y
            elif dir == '^':
                map[x - i][y] = map[x - i + 1][y]
                robot_pos = x - 1, y
        map[x][y] = '.'

sum = 0
for x, row in enumerate(map):
    for y, char in enumerate(row):
        if char == 'O':
            # is a box, calculate score
            sum += 100 * x + y

print(f"total GPS score: {sum}")  # 1414416
print(f"took {time.time() - start_time}s")
