import re

with open("input.txt") as infile:
    lines = infile.readlines()

part1 = 0

for line in lines:
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    for x, y in matches:
        part1 += (int(x) * int(y))

print(f"part1: {part1}")  # 190604937
