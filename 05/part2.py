import time
from collections import deque

start_time = time.time()

# key,val pair means for page num KEY, pages in list of val should come after
page_ordering = {}
page_updates = []

with open("input.txt") as infile:
    is_order = True
    for line in infile.readlines():
        if line == '\n':
            is_order = False
            continue

        line = line.strip()

        if is_order:
            a = [int(s) for s in line.split('|')]
            if page_ordering.get(a[0]) is None:
                page_ordering[a[0]] = [a[1]]
            else:
                page_ordering[a[0]].append(a[1])
        else:
            page_updates.append(line)

def topological_sort(update, page_ordering):
    in_degree = {page: 0 for page in update}
    for key, v in page_ordering.items():
        if key in update:
            for val in v:
                if val in in_degree:
                    in_degree[val] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_list = []

    while queue:
        page = queue.popleft()
        sorted_list.append(page)
        for after_page in page_ordering.get(page, []):
            if after_page in in_degree:
                in_degree[after_page] -= 1
                if in_degree[after_page] == 0:
                    queue.append(after_page)

    return sorted_list

val = 0

for update in page_updates:
    update = [int(_) for _ in update.split(',')]
    idx_map = {page: i for i, page in enumerate(update)}

    good_update = True
    for page in update:
        after_pages = page_ordering.get(page, [])
        for after_page in after_pages:
            if after_page in update and idx_map[after_page] < idx_map[page]:
                good_update = False
                break

        if not good_update:
            break

    if not good_update:
        sorted_update = topological_sort(update, page_ordering)
        mid_idx = len(sorted_update) // 2
        val += sorted_update[mid_idx]

print(f"val: {val}")  # 5466
print(f"took {time.time() - start_time}s")
