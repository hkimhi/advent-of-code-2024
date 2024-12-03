import pdb
import re

lines = []

with open("input.txt") as infile:
    for line in infile.readlines():
        data = [int(s) for s in re.findall(r"\d+", line)]
        lines.append(data)

n_safe = 0
n_unsafe = 0

for line in lines:
    res1 = all(i < j and j - i >= 1 and j - i <= 3 for i, j in zip(line, line[1:]))
    res2 = all(i > j and i - j >= 1 and i - j <= 3 for i, j in zip(line, line[1:]))

    if (res1 or res2):
        n_safe += 1
    else:
        n_unsafe += 1

print(n_safe)  # 202
