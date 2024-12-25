import time

start_time = time.time()

with open("input.txt") as infile:
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

# basically copied from https://shorturl.at/8v5u5
def do_the_thing(map):
    cx, cy = robot_pos

    for dir in directions:
        if dir == '^':
            dx, dy = (-1, 0)
        elif dir == '>':
            dx, dy = (0, 1)
        elif dir == 'v':
            dx, dy = (1, 0)
        elif dir == '<':
            dx, dy = (0, -1)

        to_move = [(cx, cy)]
        i = 0
        is_move_impossible = False
        # breakpoint()
        while i < len(to_move):
            x, y = to_move[i]
            nx, ny = x + dx, y + dy
            if map[nx][ny] in "[]":
                # we have a box
                if (nx, ny) not in to_move:
                    to_move.append((nx, ny))

                # get other side of box
                if map[nx][ny] == '[':
                    if (nx, ny + 1) not in to_move:
                        to_move.append((nx, ny + 1))
                elif map[nx][ny] == ']':
                    if (nx, ny - 1) not in to_move:
                        to_move.append((nx, ny - 1))
            elif map[nx][ny] == '#':
                # cannot move
                is_move_impossible = True
                break

            i += 1

        if is_move_impossible:
            continue

        map_copy = [[map[x][y] for y in range(len(map[0]))] for x in range(len(map))]
        for x, y in to_move:
            map_copy[x][y] = '.'
        for x, y in to_move:
            map_copy[x + dx][y + dy] = map[x][y]

        map = map_copy

        cx += dx
        cy += dy

    return map

map = do_the_thing(map)
sum = 0
for x, row in enumerate(map):
    for y, char in enumerate(row):
        if char == '[':
            # is a box, calculate score
            sum += 100 * x + y

print(f"total GPS score: {sum}")  # 1386070
print(f"took {time.time() - start_time}s")
