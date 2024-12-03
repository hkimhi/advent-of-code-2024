import re

with open("input.txt") as infile:
    lines = infile.readlines()

val = 0

for line in lines:
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)
    for x, y in matches:
        val += (int(x) * int(y))

print(f"val: {val}")  # 190604937
