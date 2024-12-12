import time

start_time = time.time()

with open("input.txt") as infile:
    garden = [list(line.strip()) for line in infile.readlines()]

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

"""
basic explanation:
for a corner/vertex, say the top-left one, you have two check two states
either it is

OO
OX

or

OX
XX

where X is 'plant_type' and O is 'not plant_type'

diff means 'different'
"""
def check_vertex(x, y, plant_type, vertex_type):
    if vertex_type == "top-left":
        top_diff = x == 0 or garden[x - 1][y] != plant_type
        left_diff = y == 0 or garden[x][y - 1] != plant_type
        top_left_diff = x == 0 or y == 0 or garden[x - 1][y - 1] != plant_type
        return (top_diff and left_diff) or (not top_diff and not left_diff and top_left_diff)

    elif vertex_type == "top-right":
        top_diff = x == 0 or garden[x - 1][y] != plant_type
        right_diff = y == len(garden[0]) - 1 or garden[x][y + 1] != plant_type
        top_right_diff = y == len(garden[0]) - 1 or x == 0 or garden[x - 1][y + 1] != plant_type
        return (top_diff and right_diff) or (not top_diff and not right_diff and top_right_diff)

    elif vertex_type == "bot-right":
        bot_diff = x == len(garden) - 1 or garden[x + 1][y] != plant_type
        right_diff = y == len(garden[0]) - 1 or garden[x][y + 1] != plant_type
        bot_right_diff = x == len(garden) - 1 or y == len(garden[0]) - 1 or garden[x + 1][y + 1] != plant_type
        return (bot_diff and right_diff) or (not bot_diff and not right_diff and bot_right_diff)

    elif vertex_type == "bot-left":
        bot_diff = x == len(garden) - 1 or garden[x + 1][y] != plant_type
        left_diff = y == 0 or garden[x][y - 1] != plant_type
        bot_left_diff = x == len(garden) - 1 or y == 0 or garden[x + 1][y - 1] != plant_type
        return (bot_diff and left_diff) or (not bot_diff and not left_diff and bot_left_diff)

def dfs(x, y, visited, plant_type):
    stack = [(x, y)]
    area = 0
    corners = 0

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1

        if check_vertex(cx, cy, plant_type, "top-left"):
            corners += 1
        if check_vertex(cx, cy, plant_type, "top-right"):
            corners += 1
        if check_vertex(cx, cy, plant_type, "bot-right"):
            corners += 1
        if check_vertex(cx, cy, plant_type, "bot-left"):
            corners += 1

        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(garden) and 0 <= ny < len(garden[0]) and (nx, ny) not in visited and garden[nx][ny] == plant_type:
                stack.append((nx, ny))

    return area, corners

def calculate_cost():
    visited = set()
    total_cost = 0

    for x in range(len(garden)):
        for y in range(len(garden[0])):
            if (x, y) not in visited:
                plant_type = garden[x][y]
                area, corners = dfs(x, y, visited, plant_type)
                cost = area * corners
                total_cost += cost

    return total_cost

print(f"total price: {calculate_cost()}")  # 923480
print(f"took {time.time() - start_time}s")
