import pdb

col1 = []
col2 = []

with open('input.txt') as infile:
    for line in infile.readlines():
        n = line.strip().split(' ')
        col1.append(int(n[0]))
        col2.append(int(n[3]))

col1.sort()
col2.sort()

distance = 0

for i in range(len(col1)):
    distance += abs(col1[i] - col2[i])

print(distance)
