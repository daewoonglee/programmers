from collections import deque


def solution(land):
    def bfs(xy, oil_id):
        log_xy = []
        oil = 1
        while xy:
            x, y = xy.popleft()
            log_xy.append([x, y])
            for mx, my in move:
                nx, ny = x+mx, y+my
                if 0 <= nx < N and 0 <= ny < M and land[nx][ny][0] == 1:
                    xy.append([nx, ny])
                    land[nx][ny][0] = [-1, oil_id]
                    oil += 1
        for x, y in log_xy:
            land[x][y] = [oil, oil_id]

    # get oil size
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    N, M = len(land), len(land[0])
    oil_group = -1
    for i in range(N):
        for j in range(M):
            land[i][j] = [land[i][j], oil_group]
    oil_group += 1

    for i in range(N):
        for j in range(M):
            if land[i][j][0] == 1:
                land[i][j] = [-1, oil_group]
                bfs(deque([[i, j]]), oil_group)
                oil_group += 1

    # oil drilling
    max_oil = 0
    for j in range(M):
        i = 0
        local_oil = []
        for _ in range(N):
            if land[i][j][0]:
                local_oil.append(land[i][j])
                break
            i += 1
        for z in range(i+1, N):
            if land[z][j][0] and all([1 if land[z][j][-1] != loc_oil[-1] else 0 for loc_oil in local_oil]):
                local_oil.append(land[z][j])
        max_oil = max(sum([oil for oil, _ in local_oil]), max_oil)
    return max_oil


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 9
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])) # 16
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])) # 0
print(solution([[1]])) # 1
print(solution([[0]])) # 0
print(solution([[0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 22
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 1]])) # 20
print(solution([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]])) # 17
print(solution([[1,1,1,1], [1,0,0,0], [1,0,1,0], [1,0,0,0],[1,1,1,1]])) # 12
"""
1 1 1 1 
1 0 0 0
1 0 1 0
1 0 0 0
1 1 1 1
"""
