from collections import deque


def solution(land):
    def bfs(xy, oil_cols):
        oil = 1
        col = set()
        while xy:
            x, y = xy.popleft()
            col.add(y)
            for mx, my in move_xy:
                nx, ny = x+mx, y+my
                if 0 <= nx < N and 0 <= ny < M and land[nx][ny]:
                    xy.append([nx, ny])
                    land[nx][ny] = 0
                    oil += 1
        for c in col:
            oil_cols[c] += oil

    move_xy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    N, M = len(land), len(land[0])
    oil_drilling = [0] * M
    for i in range(N):
        for j in range(M):
            if land[i][j]:
                land[i][j] = 0
                bfs(deque([[i, j]]), oil_drilling)
    return max(oil_drilling)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 9
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])) # 16
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])) # 0
print(solution([[1]])) # 1
print(solution([[0]])) # 0
print(solution([[0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 22
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 1]])) # 20
print(solution([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]])) # 17
print(solution([[1,1,1,1], [1,0,0,0], [1,0,1,0], [1,0,0,0],[1,1,1,1]])) # 12
