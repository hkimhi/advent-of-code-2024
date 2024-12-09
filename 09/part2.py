import time

start_time = time.time()

# example2.txt should have checksum = 193 (for both part1 and part2)
# example3.txt - 3964 (part2)
with open("input.txt") as infile:
    diskmap = infile.readline().strip()

alloced = []
free = []

for i, char in enumerate(list(diskmap)):
    if i % 2 == 0:
        alloced.append(int(char))
    else:
        free.append(int(char))

file_positions = []
free_positions = []
file_id = 0
for file_id, file_size in enumerate(alloced):
    block_start = sum(alloced[:file_id]) + sum(free[:file_id])
    file_positions.append((file_id, file_size, block_start))

for i, free_block_size in enumerate(free):
    block_start = sum(alloced[:i + 1]) + sum(free[:i])
    free_positions.append((free_block_size, block_start))

file_positions.sort(reverse=True)  # sort by decreasing file ID

for i, (file_id, file_size, file_block_start) in enumerate(file_positions):
    for j, (available_space, free_block_start) in enumerate(free_positions):
        if available_space >= file_size and file_block_start > free_block_start:
            # move file to this free block and update stats
            file_positions[i] = (file_id, file_size, free_block_start)
            free_positions[j] = (available_space - file_size, free_block_start + file_size)
            break

checksum = 0
for file_id, file_size, block_start in file_positions:
    for idx in range(file_size):
        # do checksum for alloced files
        checksum += (block_start + idx) * file_id

print(f"checksum: {checksum}")  # 6448168620520
print(f"took {time.time() - start_time}s")
