import time

start_time = time.time()

graph = {}

with open("input.txt") as infile:
    for line in infile.readlines():
        computer_a, computer_b = line.strip().split('-')

        if computer_a not in graph:
            graph[computer_a] = [computer_b]
        else:
            graph[computer_a].append(computer_b)

        if computer_b not in graph:
            graph[computer_b] = [computer_a]
        else:
            graph[computer_b].append(computer_a)

sets = set()

for node, adjacent in graph.items():
    if len(adjacent) == 1:
        continue

    # at least two adjacent computers
    for i in range(len(adjacent)):
        node_a = adjacent[i]
        for node_b in adjacent[i:]:
            if node_b in graph[node_a]:
                sets.add((node, node_a, node_b))

filtered = [group for group in sets if any(computer[0] == 't' for computer in group)]
print(f"length: {len(filtered) / 3}")   # 1163
print(f"took {time.time() - start_time}s")
