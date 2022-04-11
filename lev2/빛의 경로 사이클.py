def solution(grid):
    def go_to_right(x, y):
        y = 0 if y == w else y+1
        return 0, x, y

    def go_to_left(x, y):
        y = w if y == 0 else y-1
        return 1, x, y

    def go_to_up(x, y):
        x = h if x == 0 else x-1
        return 2, x, y

    def go_to_down(x, y):
        x = 0 if x == h else x+1
        return 3, x, y

    w, h = len(grid[0])-1, len(grid)-1
    print(f"w: {w}, h:{h}")
    info = [[[0]*4 for _ in g] for g in grid]
    global_cycle = []
    for d in range(4): # LRDU
        cycle = []
        i = j = 0
        while 1:
            if grid[i][j] == "S":
                if d == 0: d, i, j = go_to_right(i, j)
                elif d == 1: d, i, j = go_to_left(i, j)
                elif d == 2: d, i, j = go_to_up(i, j)
                else: d, i, j = go_to_down(i, j)
            elif grid[i][j] == "L":
                if d == 0: d, i, j = go_to_up(i, j)
                elif d == 1: d, i, j = go_to_down(i, j)
                elif d == 2: d, i, j = go_to_left(i, j)
                else: d, i, j = go_to_right(i, j)
            else:
                if d == 0: d, i, j = go_to_down(i, j)
                elif d == 1: d, i, j = go_to_up(i, j)
                elif d == 2: d, i, j = go_to_right(i, j)
                else: d, i, j = go_to_left(i, j)
            # print(f"info[i][j]: {info[i][j]}")
            if info[i][j][d]: break
            info[i][j][d] = 1
            print(f"info: {info}, d: {d}, grid: {grid[i][j]}, i: {i}, j: {j}")
            cycle.append(grid[i][j])
        print(f"cycle: {cycle}, info: {info}, global: {global_cycle}")
        if not cycle: continue
        elif global_cycle and len(cycle) > 1 and len(global_cycle[-1]) == len(cycle):
            # is same cycle
            N = len(cycle)
            for i in range(N):
                cnt = 0
                idx = i
                while cnt < N:
                    if global_cycle[-1][idx%N] != cycle[idx%N]:
                        global_cycle.append(cycle[:])
                    idx += 1
                    cnt += 1
        else:
            global_cycle.append(cycle[:])
        print(f"global: {global_cycle}")
    return [len(gc) for gc in global_cycle]


# print(solution(["SL", "LR"]))
# print(solution(["S"]))
print(solution(["R", "R"]))

