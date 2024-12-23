import time
import networkx as nx

start_time = time.time()

graph = nx.Graph()

with open("input.txt") as infile:
    for line in infile.readlines():
        computer_a, computer_b = line.strip().split('-')
        graph.add_edge(computer_a, computer_b)

max_clique = max(list(nx.find_cliques(graph)), key=len)
password = ','.join(sorted(max_clique))

print(f"password is {password}")    # bm,bo,ee,fo,gt,hv,jv,kd,md,mu,nm,wx,xh
print(f"took {time.time() - start_time}s")
