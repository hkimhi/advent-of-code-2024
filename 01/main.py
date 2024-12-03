import pdb
from collections import Counter

col1 = []
col2 = []

with open('input.txt') as infile:
    for line in infile.readlines():
        n = line.strip().split(' ')
        col1.append(int(n[0]))
        col2.append(int(n[3]))

col1.sort()
col2.sort()
count = Counter(col2)

distance = 0
similarity = 0

for i in range(len(col1)):
    n1 = col1[i]
    n2 = col2[i]
    distance += abs(n1 - n2)

    similarity += (n1 * count[n1])

print(f"distance: {distance}")      # 2815556
print(f"similarity: {similarity}")  # 23927637
