import time
from functools import cache

start_time = time.time()

with open("input.txt") as infile:
    stones = [int(_) for _ in infile.readline().strip().split(' ')]

BLINKS = 75

# how this works:
# score returns the "number of stones" that a given (stone, number of blinks) would give
# it uses memoization with the @cache decorator
# the recursion makes it really easy, especially with the decorator
# basically, for any (stone, blinks) pair, if it exists in the cache the function call will be avoided
# if it doesn't exist in the cache, we actually do the calculation then recurse down
# this allows for extreme speedup due to the super high frequency of certain (stone, blink) pairs because
#  the initial list of stones devolves into repeated (stone, blinks) pairs lower down the tree
@cache
def score(stone, blinks):
    if blinks == 0:
        return 1
    
    if stone == 0:
        return score(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return score(left, blinks - 1) + score(right, blinks - 1)
    else:
        new_stone = stone * 2024
        return score(new_stone, blinks - 1)

total_stones = sum(score(stone, BLINKS) for stone in stones)

print(f"you have: {total_stones} stones")  # 266820198587914
print(f"took {time.time() - start_time}s")
