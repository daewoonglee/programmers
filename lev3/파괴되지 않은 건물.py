def solution(board, skill):
    N, M = len(board), len(board[0])
    imos = [[0] * (M+1) for _ in range(N+1)]
    for s in skill:
        t, x1, y1, x2, y2, d = s
        d = d if t == 2 else -d
        imos[x1][y1] += d
        imos[x1][y2+1] += -d
        imos[x2+1][y1] += -d
        imos[x2+1][y2+1] += d

    for x in range(N):
        for y in range(M):
            imos[x][y+1] += imos[x][y]

    ans = 0
    for y in range(M):
        for x in range(N):
            imos[x+1][y] += imos[x][y]
            if board[x][y] + imos[x][y] > 0:
                ans += 1
    return ans


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6