def solution(grid):
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]] # LRDU
    left = {0: 2, 1: 3, 2: 1, 3: 0}
    right = {0: 3, 1: 2, 2: 0, 3: 1}
    w, h = len(grid[0]), len(grid)
    visited = [[[0]*4 for _ in g] for g in grid]
    ans = []
    for y in range(h):
        for x in range(w):
            for d in range(4): # LRDU
                # print(f"x: {x}, y: {y}, d: {d}")
                if visited[y][x][d]: continue
                ty, tx, td = y, x, d
                length = 0
                while 1:
                    length += 1
                    visited[ty][tx][td] = 1
                    if grid[ty][tx] == "L": td = left[td]
                    elif grid[ty][tx] == "R": td = right[td]
                    ty, tx = (ty+direction[td][0]) % h, (tx+direction[td][1]) % w
                    # print(f"tx: {tx}, ty: {ty}, td: {td}")
                    if tx == x and ty == y and td == d: break
                ans.append(length)
    return sorted(ans)

print(solution(["SL", "LR"])) # 	[16]
# print(solution(["S"])) # [1,1,1,1]
# print(solution(["R", "R"])) # [4,4]

