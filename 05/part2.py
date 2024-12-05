# key,val pair means for page num KEY, pages in list of val should come after
page_ordering = {}
page_updates = []

with open("example.txt") as infile:
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

val = 0

for update in page_updates:
    update = [int(_) for _ in update.split(',')]
    new_update = []
    good_update = True

    # breakpoint()

    idx_map = {page: i for i, page in enumerate(update)}

    for page in update:
        after_pages = page_ordering.get(page, [])
        for after_page in after_pages:
            if after_page in update and idx_map[after_page] < idx_map[page]:
                good_update = False
                break

        if not good_update:
            break

    if not good_update:
        # sort based on topological map
        # TODO learn more about topological map
        # basic research indicates it is a DFS that ensures dependencies are met (for any edge (u,v), u comes before v)
        sorted_update = sorted(update, key=lambda page: (idx_map.get(page, float('inf')), page))
        print(f"old: {update} | new: {sorted_update}")
        # val += new_update[len(new_update) // 2]

print(f"val: {val}")
