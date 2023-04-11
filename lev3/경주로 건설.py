from collections import deque


def solution(board):
    def bfs(x, y):
        ans = float("inf")
        search = deque([[x, y, None]])
        for i in range(len(move)):
            cost_map[x][y][i] = 0

        while search:
            x, y, d = search.popleft()
            if x == N and y == N:
                if ans > cost_map[x][y][d]:
                    ans = cost_map[x][y][d]
                continue

            for z, (mx, my) in enumerate(move):
                nx, ny = x + mx, y + my
                if 0 <= nx <= N and 0 <= ny <= N and not board[nx][ny]:
                    if d is None:
                        move_cost = 100
                    else:
                        move_cost = cost_map[x][y][d] + 100 if (d-z) % 2 == 0 else cost_map[x][y][d] + 600

                    if cost_map[nx][ny][z] > move_cost:
                        search.append([nx, ny, z])
                        cost_map[nx][ny][z] = move_cost
        return ans

    def bfs1(x, y):
        search = deque([[x, y, -1, 0]]) # x, y, dir, cost
        ans = float("inf")
        while search:
            x, y, d, c = search.popleft()
            for z, (mx, my) in enumerate(move):
                nx, ny = x + mx, y + my
                if 0 <= nx <= N and 0 <= ny <= N and not board[nx][ny]:
                    cost = c + 100 if d == -1 or (d - z) % 2 == 0 else c + 600

                    if nx == N and ny == N and ans > cost:
                        ans = cost
                    elif cost_map[nx][ny][z] > cost:
                        cost_map[nx][ny][z] = cost
                        search.append([nx, ny, z, cost])

        return ans

    N = len(board)-1
    move = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # U L D R
    cost_map = [[[float("inf")] * len(move) for _ in row] for row in board]

    # # code refactoring 01 - 0.872127471
    # return bfs(0, 0)

    # code refactoring 02 - 0.899766382
    return bfs1(0, 0)






"""
dfs 길찾기, 출발점에서 도착점 경로는 항상 가능하도록 주어짐

1. 경로 탐색하며 board에 이동 비용 저장하는 방식으로 진행
2. (0,0)에서 벽이 아닌 갈 수 있는 경로 탐색 (직선 +1)
    2-1. 이동할 방향에 있는 비용과 지금 비용을 계산하여 더 작은 값으로 갱신
3. (x,y)에서 벽이 아닌 갈 수 있는 경로 탐색
    3-1. if 이전 방향과 앞으로 나아갈 방향이 같은 경우 직선+1
         else 이전 방향과 앞으로 나아갈 방향이 다른 경우 직선+1 & 코너+1
    3-2. 이동할 방향에 있는 비용과 지금 비용을 계산하여 더 작은 값으로 갱신
4. loop 모두 탐색 시, (n-1,n-1) 값 반환
"""

# print(solution([[0,0,0],[0,0,0],[0,0,0]])) #900
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])) #3800
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) #2100
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])) #3200
print(solution([[0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]])) #4500


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
        [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
        [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]],
        [[0]*25 for _ in range(25)]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=100))
