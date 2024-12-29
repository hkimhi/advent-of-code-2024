"""
cheat MUST go through '#' tile
a_star from cheat position and see new cost, add that to prev cost

for every tile:
    know cost up until that tile
    try cheating in every direction (if available --> is there a '#' then '.' in any of [1, w, -1, -w] directions)
        if cheat was legal, run a_star from cheat position and get cheat_cost
        new cost is (cost up until that tile) + (cheat_cost) + 1?
        if new_cost < 100, add to good cheats
"""

import time
from heapq import heappush, heappop

def load_data(filename):
    with open(filename) as infile:
        data = infile.read()
        width, height = data.index('\n'), data.count('\n')
        map = data.replace('\n', '')

    return map, (width, height)

def a_star(map, width, height):
    DIRECTIONS = [1, width, -1, -width]

    start = map.index("S")
    end = map.index("E")
    # xs, ys = start // w, start % w
    xe, ye = end // width, end % width

    def h(pos):
        x, y = pos // width, pos % width
        return abs(x - xe) + abs(y - ye)

    costs = {}
    costs[start] = 0

    pq = []
    heappush(pq, (0, start, 0, []))  # cost, pos, moves, path

    while pq:
        cost, pos, moves, path = heappop(pq)
        if pos == end:
            path_and_cost = [(start, 0)]  # inital start position
            for i in range(len(path)):
                path_and_cost += [(path[i], i + 1)]  # tile and cost at that tile
            return moves, path_and_cost

        for d in DIRECTIONS:
            npos = pos + d
            if 0 <= npos < (width * height) and map[npos] != '#':
                ncost = cost + 1
                if npos not in costs or ncost < costs[npos]:
                    costs[npos] = ncost
                    heappush(pq, (ncost + h(npos), npos, moves + 1, [*path, npos]))

    return float('inf')

def cheating_a_star(map, width, height, path, base_cost):
    DIRECTIONS = [1, width, -1, -width]

    start = map.index("S")
    end = map.index("E")
    map = map[:end] + '.' + map[end + 1:]  # replace "E" with '.'
    xe, ye = end // width, end % width

    def h(pos):
        x, y = pos // width, pos % width
        return abs(x - xe) + abs(y - ye)

    num_cheats = 0
    for tile, tile_cost in path:
        costs = {}
        costs[start] = 0
        pq = []

        # attempt a cheat
        for d_cheat in DIRECTIONS:
            ntile = tile + d_cheat
            nntile = tile + 2 * d_cheat
            in_bounds = 0 <= ntile, nntile < width * height
            if all(in_bounds) and map[ntile] == '#' and map[nntile] == '.':
                # cheat possible
                heappush(pq, (0, nntile, tile_cost + 2))

                # run a_star from new location (after cheating)
                while pq:
                    cost, pos, moves = heappop(pq)
                    if pos == end:
                        if base_cost - moves > 100:
                        # if moves < base_cost:
                            # print(f"good cheat saving {base_cost - moves}ps from {tile} to {nntile} in dir {d_cheat}")
                            # print(f"good cheat saving {base_cost - moves}ps from ({tile // width}, {tile % width}) to ({nntile // width}, {nntile % width}) in dir {d_cheat}")
                            num_cheats += 1
                        break

                    for d in DIRECTIONS:
                        npos = pos + d
                        if 0 <= npos < (width * height) and map[npos] != '#':
                            ncost = cost + 1
                            if npos not in costs or ncost < costs[npos]:
                                costs[npos] = ncost
                                heappush(pq, (ncost + h(npos), npos, moves + 1))

    return num_cheats

if __name__ == "__main__":
    start_time = time.time()

    map, (w, h) = load_data("input.txt")
    optimal_path_length, path = a_star(map, w, h)
    num_good_cheats = cheating_a_star(map, w, h, path, optimal_path_length)
    # print(f"optimal path length: {optimal_path_length}")
    print(f"number of cheats: {num_good_cheats}")  # example.txt --> 44

    print(f"took {time.time() - start_time}s")
