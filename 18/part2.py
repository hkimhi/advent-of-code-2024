from heapq import heappush, heappop
import time

start_time = time.time()

def load_data(filename):
    with open(filename) as infile:
        data = infile.read().strip().split('\n')
    return data

def simulate_fall(data, length, num_falling):
    grid = [['.' for _ in range(length)] for _ in range(length)]
    for i in range(num_falling):
        x, y = list(map(int, data[i].split(',')))
        grid[y][x] = '#'

    return grid

def a_star(maze, start, end):
    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    xs, ys = start
    xe, ye = end

    def heuristic(x, y):
        return abs(xe - x) + abs(ye - y)

    pq = []
    # cost, position (x, y), moves
    heappush(pq, (0, start, 0))

    costs = {}
    costs[start] = 0

    while pq:
        cost, pos, moves = heappop(pq)
        if pos == end:
            return moves

        for dx, dy in DIRECTIONS:
            nx, ny = pos[0] + dx, pos[1] + dy
            if 0 <= nx <= xe and 0 <= ny <= ye and maze[nx][ny] != '#':
                ncost = cost + 1
                if (nx, ny) not in costs or ncost < costs[(nx, ny)]:
                    costs[(nx, ny)] = ncost
                    heappush(pq, (ncost + heuristic(nx, ny), (nx, ny), moves + 1))

    return float('inf')

def find_first_bad_byte(filepath, length):
    data = load_data(filepath)
    for i in range(len(data)):
        map = simulate_fall(data, length, i + 1)
        shortest_path_length = a_star(map, (0, 0), (length - 1, length - 1))
        if shortest_path_length == float('inf'):
            return data[i]

    return (-1, -1)

# bad_byte = find_first_bad_byte("example.txt", 7)
bad_byte = find_first_bad_byte("input.txt", 71)

print(f"bad byte: {bad_byte}")  # 16, 46
print(f"took {time.time() - start_time}s")
