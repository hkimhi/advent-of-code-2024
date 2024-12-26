from heapq import heappush, heappop
import time
from math import inf

start_time = time.time()

DIRECTIONS = [
    (0, 1),   # east
    (1, 0),   # south
    (0, -1),  # west
    (-1, 0)   # north
]

ROTATIONS = [1, -1]  # clockwise, counterclockwise (90 degrees each)

with open("input.txt") as infile:
    maze = [list(line) for line in infile.read().strip().split('\n')]

def dijkstra(start, end):
    x_start, y_start = start
    x_end, y_end = end

    visited = {}
    max_score = inf
    paths = []
    pq = []
    # cost, position (x,y), distance, direction, path
    heappush(pq, (0, start, 0, ""))

    while pq:
        score, position, direction, path = heappop(pq)
        if score > max_score:
            # bad path
            continue
        if (position, direction) in visited and visited[(position, direction)] < score:
            # have been here before, and got to this position with a smaller score in the past
            continue
        visited[(position, direction)] = score
        if position == end:
            max_score = score
            paths.append(path)
        if maze[position[0]][position[1]] != '#':
            x, y = position[0] + DIRECTIONS[direction][0], position[1] + DIRECTIONS[direction][1]
            heappush(pq, (score + 1, (x, y), direction, path + "F"))
        heappush(pq, (score + 1000, position, (direction + 1) % 4, path + "R"))
        heappush(pq, (score + 1000, position, (direction - 1) % 4, path + "L"))

    return paths

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

optimal_paths = dijkstra(start, end)
score = 0
for char in optimal_paths[0]:
    if char == 'F':
        score += 1
    elif char in "LR":
        score += 1000

tiles = set()
tiles.add(start)
for path in optimal_paths:
    tile, dir = (start, 0)
    for char in path:
        if char == "L":
            dir = (dir - 1) % 4
        elif char == "R":
            dir = (dir + 1) % 4
        elif char == "F":
            tile = tile[0] + DIRECTIONS[dir][0], tile[1] + DIRECTIONS[dir][1]
            tiles.add(tile)

print(f"best score: {score}")  # 79404
print(f"num optimal seating locations: {len(tiles)}")  # 451
print(f"Took {time.time() - start_time}s")
