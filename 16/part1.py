import heapq
import time

start_time = time.time()

DIRECTIONS = [
    (0, 1),   # east
    (1, 0),   # south
    (0, -1),  # west
    (-1, 0)   # north
]

# clockwise, counter clockwise (90 degrees each)
ROTATIONS = [1, -1]

with open("input.txt") as infile:
    maze = [list(line) for line in infile.read().strip().split('\n')]

def heuristic(x, y, x_end, y_end):
    return abs(x_end - x) + abs(y_end - y)

def a_star(start, end):
    x_start, y_start = start
    x_end, y_end = end

    priority_queue = []
    # priority_queue has (cost, x, y, direction, moves, rotations)
    # cost is from the heuristic, actual_cost in the return value is the 'true' value
    heapq.heappush(priority_queue, (0, x_start, y_start, 0, 0, 0))  # Start facing east

    costs = {}
    costs[(x_start, y_start, 0)] = 0  # Start facing east

    while priority_queue:
        cost, x, y, dir, moves, rotations = heapq.heappop(priority_queue)

        if (x, y) == (x_end, y_end):
            # finished the maze
            actual_cost = rotations * 1000 + moves
            return actual_cost

        # move forward
        nx, ny = x + DIRECTIONS[dir][0], y + DIRECTIONS[dir][1]
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#':
            ncost = cost + 1
            if (nx, ny, dir) not in costs or ncost < costs[(nx, ny, dir)]:
                costs[(nx, ny, dir)] = ncost
                heapq.heappush(priority_queue, (ncost + heuristic(nx, ny, x_end, y_end), nx, ny, dir, moves + 1, rotations))

        # rotate
        for rotation in ROTATIONS:
            ndir = (dir + rotation) % 4
            ncost = cost + 1000
            if (x, y, ndir) not in costs or ncost < costs[(x, y, ndir)]:
                costs[(x, y, ndir)] = ncost
                heapq.heappush(priority_queue, (ncost + heuristic(x, y, x_end, y_end), x, y, ndir, moves, rotations + 1))

    return float('inf')

start = None
end = None
for x, row in enumerate(maze):
    for y, char in enumerate(row):
        if char == 'S':
            start = (x, y)
        elif char == 'E':
            end = (x, y)
    if start and end:
        break

smallest_score = a_star(start, end)
print(f"lowest score: {smallest_score}")  # 79404
print(f"took {time.time() - start_time}s")
