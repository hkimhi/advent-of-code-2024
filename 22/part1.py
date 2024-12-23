import time

start_time = time.time()

with open("input.txt") as infile:
    initial_numbers = [int(_) for _ in infile.read().split('\n')[:-1]]

def mix(num, other):
    return num ^ other

def prune(num):
    return num % 16777216

def gen_next(num):
    num = prune(mix(num, num * 64))
    num = prune(mix(num, num // 32))
    num = prune(mix(num, num * 2048))

    return num

sum = 0
for num in initial_numbers:
    for _ in range(2000):
        num = gen_next(num)
    sum += num

print(f"val: {sum}")    # 17262627539
print(f"took {time.time() - start_time}s")
