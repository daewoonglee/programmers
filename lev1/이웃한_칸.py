def solution(board, h, w):
    ans = 0
    N = len(board)

    # if h+1 < N and board[h][w] == board[h+1][w]:
    #     ans += 1
    # if h-1 >= 0 and board[h][w] == board[h-1][w]:
    #     ans += 1
    # if w+1 < N and board[h][w] == board[h][w+1]:
    #     ans += 1
    # if w-1 >= 0 and board[h][w] == board[h][w-1]:
    #     ans += 1

    yh, xw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(4):
        dh, dw = h + yh[i], w + xw[i]
        if 0 <= dh < N and 0 <= dw < N:
            if board[h][w] == board[dh][dw]:
                ans += 1

    return ans


print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1)) # 2
print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1)) # 1
