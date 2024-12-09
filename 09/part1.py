import time

start_time = time.time()

with open("input.txt") as infile:
    diskmap = infile.readline().strip()

alloced = []
free = []

for i, char in enumerate(list(diskmap)):
    if i % 2 == 0:
        alloced.append(int(char))
    else:
        free.append(int(char))

compacting = []
add_alloced = True

idx_alloc_start = 0
idx_alloc_end = len(alloced) - 1
idx_free = 0

while True:
    if idx_alloc_start > idx_alloc_end:
        break

    if add_alloced:
        compacting += [idx_alloc_start] * alloced[idx_alloc_start]
        idx_alloc_start += 1

        if idx_free < len(free):
            add_alloced = not add_alloced
    else:
        available_space = free[idx_free]
        block_size = alloced[idx_alloc_end]
        times_to_add = min(available_space, block_size)

        compacting += [idx_alloc_end] * times_to_add

        if times_to_add == block_size:
            # last block is now completely moved over
            # next iteration will move the next last black
            idx_alloc_end -= 1
            free[idx_free] -= times_to_add
        else:
            # we ran out of free space
            alloced[idx_alloc_end] -= times_to_add
            idx_free += 1
            add_alloced = not add_alloced  # switch to adding alloc'd blocks

checksum = 0
for idx, file_id in enumerate(compacting):
    checksum += idx * file_id

print(f"checksum: {checksum}")  # 6421128769094
print(f"took {time.time() - start_time}s")
