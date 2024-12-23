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

# total_bananas stores key: sequence -> val: total number of bananas gotten by telling all monkeys that sequence
total_bananas = defaultdict(int)
# breakpoint()
for num in initial_numbers:
    sequences = {}  # for the current monkey
    sequence = (0, 0, 0, 0)  # initial sequence is no price changes
    for i in range(2000):
        previous_bananas = num % 10
        num = gen_next(num)
        current_bananas = num % 10
        sequence = (*sequence[1:], current_bananas - previous_bananas)

        # if we have a valid sequence (at least 3 price changes), add it to the dict
        # sequences stores key: sequence -> val: num bananas
        if i >= 3 and sequence not in sequences:
            sequences[sequence] = current_bananas
            total_bananas[sequence] += current_bananas  # total number of bananas for this sequence across all monkeys

# get the highest number of bananas possible (and the sequence that arrived there if we want it)
best = sorted([(value, key) for key, value in total_bananas.items()])[-1]

print(best)    # 1986
print(f"took {time.time() - start_time}s")
