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
                if 0 <= nx < N and 0 <= ny < M and land[nx][ny][0]:
                    xy.append([nx, ny])
                    land[nx][ny][0] = 0
                    oil += 1
        for x, y in log_xy:
            land[x][y] = [oil, oil_id]

    # get oil size
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    N, M = len(land), len(land[0])
    for i in range(N):
        for j in range(M):
            land[i][j] = [land[i][j], -1]

    oil_group = 0
    for i in range(N):
        for j in range(M):
            if land[i][j][0] == 1:
                land[i][j] = [0, oil_group]
                bfs(deque([[i, j]]), oil_group)
                oil_group += 1

    # oil drilling
    max_oil = 0
    for j in range(M):
        local_sum = 0
        local_oil_log = []
        for i in range(N):
            if land[i][j][0]:
                land_id = land[i][j][1]
                for gid in local_oil_log:
                    if land_id == gid: break
                else:
                    local_oil_log.append(land_id)
                    local_sum += land[i][j][0]
        max_oil = local_sum if local_sum > max_oil else max_oil

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
