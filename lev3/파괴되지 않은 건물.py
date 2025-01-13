def solution(board, skill):
    # 1, 효율 0
    for s in skill:
        t, x1, y1, x2, y2, d = s
        d = d if t == 2 else -d
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] += d

    ans = 0
    for row in board:
        for r in row:
            if r > 0:
                ans += 1
    return ans


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6