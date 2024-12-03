import pdb
import re

lines = []

with open("input.txt") as infile:
    for line in infile.readlines():
        data = [int(s) for s in re.findall(r"\d+", line)]
        lines.append(data)

n_safe = 0

def is_safe(line):
    res1 = all(i < j and j - i >= 1 and j - i <= 3 for i, j in zip(line, line[1:]))
    res2 = all(i > j and i - j >= 1 and i - j <= 3 for i, j in zip(line, line[1:]))

    return res1 or res2

for line in lines:
    if (is_safe(line)):
        n_safe += 1
    else:
        found_safe = False
        for i in range(len(line)):
            new_line = line[:i] + line[i + 1:]
            if is_safe(new_line):
                found_safe = True
                n_safe += 1
                break

print(n_safe)  # 271
