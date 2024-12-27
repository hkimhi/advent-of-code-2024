import time
from functools import cache

start_time = time.time()

def load_data(pathname):
    with open(pathname) as infile:
        data = infile.read().strip().split('\n\n')

    towels = data[0].split(', ')
    desired_designs = data[1].split('\n')
    return towels, desired_designs

@cache
def count_arrangements(design, towels):
    if design == "":
        return 1

    num_arrangements = 0
    for towel in towels:
        if design.startswith(towel):
            num_arrangements += count_arrangements(design[len(towel):], towels)

    return num_arrangements

def solve(towels, designs):
    count = 0

    for design in designs:
        count += count_arrangements(design, tuple(towels))

    return count


towels, desired_patterns = load_data("input.txt")
print(f"Number of possible designs: {solve(towels, desired_patterns)}")  # 565600047715343
print(f"Took {time.time() - start_time}s")
