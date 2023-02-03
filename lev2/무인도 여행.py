def solution(maps):
    def dfs(r, c, cnt):
        if not searched[r][c]:
            return cnt
        searched[r][c] = 0

        if r-1 >= 0: # 상
            cnt = dfs(r-1, c, cnt)
        if r+1 < ROWS: # 하
            cnt = dfs(r+1, c, cnt)
        if c-1 >= 0: # 좌
            cnt = dfs(r, c-1, cnt)
        if c+1 < COLS: # 우
            cnt = dfs(r, c+1, cnt)

        return int(maps[r][c]) + cnt

    ROWS, COLS = len(maps), len(maps[0])
    searched = [[1 if r != "X" else 0 for r in row] for row in maps]
    print(searched)

    ans = []
    for i in range(len(searched)):
        for j in range(len(searched[i])):
            if searched[i][j]:
                ans.append(dfs(i, j, 0))

    return [-1] if not ans else sorted(ans)



"""
    0 1 2 3 4
    ---------
0 | X 5 9 1 X
1 | X 1 X 5 X
2 | X 2 3 1 X
3 | 1 X X X 1
"""

print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1,1,27]
# print(solution(["XXX","XXX","XXX"])) # [-1]
