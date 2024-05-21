def solution(land):
    def bfs(xy, oil_id):
        log_xy = []
        oil = 1
        while xy:
            x, y = xy.pop(0)
            log_xy.append([x, y])
            for mx, my in move:
                nx, ny = x+mx, y+my
                if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1:
                    xy.append([nx, ny])
                    land[nx][ny] = [-1, oil_id]
                    oil += 1
        for x, y in log_xy:
            land[x][y] = [oil, oil_id]

    # get oil size
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    N, M = len(land), len(land[0])
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                land[i][j] = -1
                bfs([[i, j]], f"{i}_{j}")

    # oil drilling
    max_oil = 0
    for j in range(M):
        local_oil = []
        for i in range(N):
            if isinstance(land[i][j], list) and (not local_oil or all([1 if land[i][j][-1] != loc_oil[-1] else 0 for loc_oil in local_oil])):
                local_oil.append(land[i][j])
        sum_oil = sum([oil for oil, _ in local_oil]) if local_oil else 0
        max_oil = sum_oil if sum_oil > max_oil else max_oil
    return max_oil


# print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 9
# print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])) # 16
# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])) # 0
# print(solution([[1]])) # 1
# print(solution([[0]])) # 0
# print(solution([[0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 22
# print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 1]])) # 20
# print(solution([[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]])) # 17
print(solution([[1,1,1,1], [1,0,0,0], [1,0,1,0], [1,0,0,0],[1,1,1,1]])) # 12
"""
1 1 1 1 
1 0 0 0
1 0 1 0
1 0 0 0
1 1 1 1
"""
