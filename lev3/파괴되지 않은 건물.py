def solution(board, skill):
    # 효율성 (0/7)
    # for s in skill:
    #     t, x1, y1, x2, y2, d = s
    #     d = d if t == 2 else -d
    #     row = x2 - x1 + 1
    #     col = y2 - y1 + 1
    #     for i in range(row*col):
    #         x, y = x1+i//col, y1+i%col
    #         board[x][y] += d
    #
    # ans = 0
    # for row in board:
    #     for r in row:
    #         if r > 0:
    #             ans += 1
    # return ans

    # 효율성 (0/7)
    ans = len(board) * len(board[0])
    flag = [[1]*len(board[0]) for _ in board]
    for s in skill:
        t, x1, y1, x2, y2, d = s
        d = d if t == 2 else -d
        row = x2-x1+1
        col = y2-y1+1
        for i in range(row*col):
            x, y = x1+i//col, y1+i%col
            board[x][y] += d
            if board[x][y] <= 0 and flag[x][y]:
                ans -= 1
                flag[x][y] = 0
            elif board[x][y] > 0 and not flag[x][y]:
                ans += 1
                flag[x][y] = 1
    return ans




print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6