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

val = 0

for update in page_updates:
    update = [int(_) for _ in update.split(',')]
    good_page = True

    for i, page in enumerate(update):
        for after_pages in page_ordering.get(page):
            if after_pages in update[:i]:
                good_page = False
                # breakpoint()
                break

        if not good_page:
            # breakpoint()
            break

    if good_page:
        val += update[len(update) // 2]

print(f"val: {val}")  # 4281
