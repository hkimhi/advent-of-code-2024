from collections import defaultdict
import time

start_time = time.time()

with open("input.txt") as infile:
    initial_numbers = [int(_) for _ in infile.read().split('\n')[:-1]]

def gen_next(num):
    def mix(num, other):
        return num ^ other

    def prune(num):
        return num % 16777216

    num = prune(mix(num, num * 64))
    num = prune(mix(num, num // 32))
    num = prune(mix(num, num * 2048))

    return num

total_bananas = defaultdict(int)
for num in initial_numbers:
    sequences = {}
    sequence = (0, 0, 0, 0)
    for i in range(2000):
        previous_bananas = num % 10
        num = gen_next(num)
        current_bananas = num % 10
        sequence = (*sequence[1:], current_bananas - previous_bananas)
        if i >= 3 and sequence not in sequences:
            sequences[sequence] = current_bananas
    for seq in sequences:
        total_bananas[seq] += sequences[seq]

best = sorted([(value, key) for key, value in total_bananas.items()])[-1]

print(best)    # 1986
print(f"took {time.time() - start_time}s")
