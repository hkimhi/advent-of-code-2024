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

def dfs(x, y, visited, plant_type):
    stack = [(x, y)]
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        local_perimeter = 4

        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(garden) and 0 <= ny < len(garden[0]):
                if garden[nx][ny] == plant_type:
                    stack.append((nx, ny))
                    local_perimeter -= 1

        perimeter += local_perimeter

    return area, perimeter

def calculate_cost():
    visited = set()
    total_cost = 0

    for x in range(len(garden)):
        for y in range(len(garden[0])):
            if (x, y) not in visited:
                plant_type = garden[x][y]
                area, perimeter = dfs(x, y, visited, plant_type)
                cost = area * perimeter
                total_cost += cost

    return total_cost

print(f"total price: {calculate_cost()}")  # 1477762
print(f"took {time.time() - start_time}s")
