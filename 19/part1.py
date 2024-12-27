# https://en.wikipedia.org/wiki/Trie
import time

start_time = time.time()

def load_data(pathname):
    with open(pathname) as infile:
        data = infile.read().strip().split('\n\n')

    towels = data[0].split(', ')
    desired_designs = data[1].split('\n')
    return (towels, desired_designs)

def build_trie(towels):
    trie = {}
    for towel in towels:
        node = trie
        for char in towel:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True  # end of towel pattern
    return trie

def can_form_design(trie, design):
    depth = len(design)
    memo = [False] * (depth + 1)
    memo[0] = True

    for i in range(depth):
        if not memo[i]:
            continue

        node = trie
        j = i
        while j < depth and design[j] in node:
            node = node[design[j]]
            j += 1
            if '*' in node:
                # '*' for end of design
                memo[j] = True

    return memo[depth]

def solve(towels, desired):
    trie = build_trie(towels)
    count = 0

    for design in desired:
        if can_form_design(trie, design):
            count += 1

    return count

towels, desired_patterns = load_data("input.txt")
print(f"num possible designs: {solve(towels, desired_patterns)}")  # 220
print(f"took {time.time() - start_time}s")
