import time
import itertools

data = []

with open("input.txt") as infile:
    data = [line.strip() for line in infile.readlines()]

start_time = time.time()

antenna_positions = set()
antenna_map = {}

for x, row in enumerate(data):
    for y, char in enumerate(row):
        if char != '.':
            antenna = char
            if antenna_map.get(char) is None:
                antenna_map[char] = [(x, y)]
            else:
                antenna_map[char].append((x, y))
            antenna_positions.add((x, y))

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

        if x1 <= x2 and y1 <= y2:
            if 0 <= xn1 < len(data) and 0 <= yn1 < len(data[0]):
                antinode_positions.add((xn1, yn1))
            if 0 <= xn2 < len(data) and 0 <= yn2 < len(data[0]):
                antinode_positions.add((xn2, yn2))
        else:
            if 0 <= xn1 < len(data) and 0 <= yn2 < len(data[0]):
                antinode_positions.add((xn1, yn2))
            if 0 <= xn2 < len(data) and 0 <= yn1 < len(data[0]):
                antinode_positions.add((xn2, yn1))

print(f"len(antinode_positions): {len(antinode_positions)}")  # 379
print(f"took {time.time() - start_time}s")
