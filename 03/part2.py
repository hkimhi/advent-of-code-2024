import re

with open("input.txt") as infile:
    lines = infile.readlines()

part2 = 0
mul_enabled = True

for line in lines:
    regex_string = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
    tokens = re.split(regex_string, line)
    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        elif token.startswith("mul"):
            match = re.match(r"mul\((\d+),(\d+)\)", token)

            if mul_enabled and match is not None:
                x, y = match.groups()
                part2 += (int(x) * int(y))

print(f"part2: {part2}")  # 82857512
