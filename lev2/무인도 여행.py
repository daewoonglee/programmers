import sys
sys.setrecursionlimit(10000) # 100x100


def solution(maps):
    def dfs(r, c, cnt):
        searched[r][c] = 0

        if r-1 >= 0 and searched[r-1][c]: # 상
            cnt = dfs(r-1, c, cnt)
        if r+1 < ROWS and searched[r+1][c]: # 하
            cnt = dfs(r+1, c, cnt)
        if c-1 >= 0 and searched[r][c-1]: # 좌
            cnt = dfs(r, c-1, cnt)
        if c+1 < COLS and searched[r][c+1]: # 우
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
    0 1 2 3 4 5
    -----------
0 | X 5 X X X 1
1 | X 1 X 5 1 1
2 | X 2 3 X X X
3 | 1 X X X 1 X
"""

# print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1,1,27]
# print(solution(["X591XX", "X1X511", "X231XX", "1XXX1X"])) # [1,1,29]
print(solution(["X5XXX1", "X1X511", "X23XXX", "1XXX1X"])) # [1,1,8,11]
# print(solution(["XXX","XXX","XXX"])) # [-1]
