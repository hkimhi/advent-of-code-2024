import time

start_time = time.time()

with open("input.txt") as infile:
    stones = [int(_) for _ in infile.readline().strip().split(' ')]

BLINKS = 25

for i in range(BLINKS):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            # stone is even length
            length = len(str(stone))
            stone_left = int(str(stone)[:length // 2])
            stone_right = int(str(stone)[length // 2:])
            new_stones.append(stone_left)
            new_stones.append(stone_right)
        else:
            new_stones.append(stone * 2024)
    stones = new_stones

print(f"you have: {len(stones)} stones")  # 224529
print(f"took {time.time() - start_time}s")
