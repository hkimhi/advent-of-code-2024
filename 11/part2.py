import time
from functools import lru_cache

start_time = time.time()

with open("input.txt") as infile:
    stones = [int(_) for _ in infile.readline().strip().split(' ')]

BLINKS = 75

@lru_cache(None)
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
