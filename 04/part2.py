# target word = XMAS
TARGET = "MAS"

with open("input.txt") as infile:
    lines = infile.readlines()

# convert strings to lists for easy char access
lines = [list(line) for line in lines]

occurrences = 0

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        char = lines[i][j]
        if (char == 'A'):
            # check if diagonals have "M" or "S"

            UL = lines[i - 1][j - 1]
            UR = lines[i - 1][j + 1]
            DL = lines[i + 1][j - 1]
            DR = lines[i + 1][j + 1]

            if ((UL == "M" and DR == "S") or (UL == "S" and DR == "M")) and ((UR == "M" and DL == "S") or (UR == "S" and DL == "M")):
                occurrences += 1

print(f"Count: {occurrences}")  # 1936
