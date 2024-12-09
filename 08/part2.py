import time
import itertools

data = []

with open("input.txt") as infile:
    data = [line.strip() for line in infile.readlines()]

start_time = time.time()

antenna_map = {}

for x, row in enumerate(data):
    for y, char in enumerate(row):
        if char != '.':
            antenna = char
            if antenna_map.get(char) is None:
                antenna_map[char] = [(x, y)]
            else:
                antenna_map[char].append((x, y))

antinode_positions = set()

for val in antenna_map.values():
    pairs = list(itertools.combinations(val, 2))
    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        xn1 = min(x1, x2) - dx
        xn2 = max(x1, x2) + dx
        yn1 = min(y1, y2) - dy
        yn2 = max(y1, y2) + dy

        antinode_positions.add((x1, y1))
        antinode_positions.add((x2, y2))

        slope_decreasing = True if (x1 <= x2 and y1 <= y2) else False

        while True:
            if slope_decreasing:
                generate_point1 = 0 <= xn1 < len(data) and 0 <= yn1 < len(data[0])
                generate_point2 = 0 <= xn2 < len(data) and 0 <= yn2 < len(data[0])
            else:
                generate_point1 = 0 <= xn1 < len(data) and 0 <= yn2 < len(data[0])
                generate_point2 = 0 <= xn2 < len(data) and 0 <= yn1 < len(data[0])

            if not generate_point1 and not generate_point2:
                break

            if slope_decreasing:
                if generate_point1:
                    point_back = (xn1, yn1)
                    antinode_positions.add(point_back)
                    xn1 -= dx
                    yn1 -= dy
                if generate_point2:
                    point_forward = (xn2, yn2)
                    antinode_positions.add(point_forward)
                    xn2 += dx
                    yn2 += dy
            else:
                if generate_point1:
                    point_back = (xn1, yn2)
                    antinode_positions.add(point_back)
                    xn1 -= dx
                    yn2 += dy
                if generate_point2:
                    point_forward = (xn2, yn1)
                    antinode_positions.add(point_forward)
                    xn2 += dx
                    yn1 -= dy

print(f"len(antinode_positions): {len(antinode_positions)}")  # 1339
print(f"took {time.time() - start_time}s")
