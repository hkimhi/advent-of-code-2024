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

def move(grid, start_pos, direction):
    visited = set()

    x, y = start_pos
    visited.add((x, y, direction))

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

            if (x, y, direction) in visited:
                # in a loop
                return True

            visited.add((x, y, direction))

    return False

def test_new_obstruction(grid, start_pos, direction, obstruction_position):
    grid_copy = [row[:] for row in grid]
    x, y = obstruction_position
    grid_copy[x][y] = '#'
    is_loop = move(grid_copy, start_pos, direction)
    return is_loop

def find_new_obstructions(grid, start_pos, direction):
    possible_positions = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (i, j) != start_pos:
                if test_new_obstruction(grid, start_pos, direction, (i, j)):
                    possible_positions.add((i, j))
    return possible_positions


print(f"possible new obstruction positions: {len(find_new_obstructions(grid, start_pos, direction))}")
# answer is 1480, but the naive solution of checking every single square is quite slow (though it does work)

