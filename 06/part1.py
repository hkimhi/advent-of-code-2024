grid = []
direction = '^'

with open("input.txt") as infile:
    for i, line in enumerate(infile.readlines()):
        line = line.strip()
        row = list(line)
        grid.append(row)

        for j, character in enumerate(row):
            if character == '^':
                start_pos = (i, j)


directions = {
    '^': (-1, 0),   # up one, same col
    'v': (1, 0),    # down onw row, same col
    '>': (0, 1),    # same row, one col right
    '<': (0, -1)    # same row, one col left
}
turns = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

visited = set()

x, y = start_pos
visited.add((x, y))

while (True):
    dx, dy = directions[direction]
    new_x, new_y = x + dx, y + dy

    if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
        # exited the map
        break

    if grid[new_x][new_y] == '#':
        # rotate guard
        direction = turns[direction]
    else:
        # move guard
        x, y = new_x, new_y
        visited.add((x, y))

        grid[x][y] = 'X'

    # breakpoint()
    # for row in grid:
        # print(''.join(row))


print(f"num visited blocks: {len(visited)}")  # 4580
