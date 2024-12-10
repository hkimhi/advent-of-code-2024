import time

start_time = time.time()

with open("input.txt") as infile:
    grid = [list(int(_) for _ in line.strip()) for line in infile.readlines()]

trailheads = []
for x, row in enumerate(grid):
    for y, col in enumerate(row):
        if col == 0:
            trailheads.append((x, y))

def dfs(x, y, visited):
    # from (x,y), return how many trailends can be reached with a legal hiking trail
    # a legal hiking trip has an increment of 1 every step until 9
    if (x, y) in visited:
        return 0

    visited.add((x, y))

    if grid[x][y] == 9:
        visited.remove((x, y))
        return 1

    trail_count = 0
    directions = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == grid[x][y] + 1:
                trail_count += dfs(nx, ny, visited)

    visited.remove((x, y))

    return trail_count

trailhead_score = 0
for x, y in trailheads:
    trailhead_score += dfs(x, y, set())

print(f"sum: {trailhead_score}")
print(f"took {time.time() - start_time}s")
