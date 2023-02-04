from collections import deque
import sys
sys.setrecursionlimit(10000) # 100x100


def solution(maps):
    # # 0.390103734
    # def dfs(x, y, food):
    #     visited[x][y] = 1
    #
    #     if x-1 >= 0 and not visited[x-1][y]: # 상
    #         food = dfs(x-1, y, food)
    #     if x+1 < ROWS and not visited[x+1][y]: # 하
    #         food = dfs(x+1, y, food)
    #     if y-1 >= 0 and not visited[x][y-1]: # 좌
    #         food = dfs(x, y-1, food)
    #     if y+1 < COLS and not visited[x][y+1]: # 우
    #         food = dfs(x, y+1, food)
    #
    #     return int(maps[x][y]) + food
    #
    # ROWS, COLS = len(maps), len(maps[0])
    # visited = [[0 if r != "X" else 1 for r in row] for row in maps]
    #
    # ans = []
    # for i in range(ROWS):
    #     for j in range(COLS):
    #         if not visited[i][j]:
    #             ans.append(dfs(i, j, 0))
    #
    # return [-1] if not ans else sorted(ans)

    # code refactoring (bfs) - 0.426967768
    def bfs(x, y, food):
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue.append((x, y))
        visited[x][y] = 1
        while queue:
            x, y = queue.popleft()
            for mx, my in move:
                nx, ny = x + mx, y + my
                if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    food += int(maps[nx][ny])
        queue.clear()
        return food

    ROWS, COLS = len(maps), len(maps[0])
    visited = [[0 if r != "X" else 1 for r in row] for row in maps]
    ans = []
    queue = deque()
    for i in range(ROWS):
        for j in range(COLS):
            if not visited[i][j]:
                ans.append(bfs(i, j, int(maps[i][j])))

    return sorted(ans) if ans else [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1,1,27]
print(solution(["X591XX", "X1X511", "X231XX", "1XXX1X"])) # [1,1,29]
# print(solution(["X5XXX1", "X1X511", "X23XXX", "1XXX1X"])) # [1,1,8,11]
# print(solution(["XXX","XXX","XXX"])) # [-1]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        ["X591X","X1X5X","X231X", "1XXX1"],
        ["X591XX", "X1X511", "X231XX", "1XXX1X"],
        ["X5XXX1", "X1X511", "X23XXX", "1XXX1X"],
        ["XXX","XXX","XXX"],
        ["X5XXX1"*10, "X1X511"*10, "X23XXX"*10, "1XXX1X"*10],
        ["XXX"*30,"XXX"*30,"XXX"*30]*10,
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))
