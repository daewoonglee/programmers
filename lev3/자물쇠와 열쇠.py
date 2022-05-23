def solution(key, lock):
    def rotate():
        return list(zip(*key[::-1]))

    def attach():
        for i in range(M):
            for j in range(M):
                board[x+i][y+j] += key[i][j]

    def detach():
        for i in range(M):
            for j in range(M):
                board[x+i][y+j] -= key[i][j]

    def match():
        for i in range(N):
            for j in range(N):
                if board[i+M][j+M] != 1: return False
        return True

    M, N = len(key), len(lock)
    board = [[0] * (N*3) for _ in range(N*3)]
    for i in range(N):
        for j in range(N):
            board[i+M][j+M] = lock[i][j]

    for _ in range(4):
        for x in range(1, N+M):
            for y in range(1, N+M):
                attach()
                if match(): return True
                detach()
        key = rotate()
    return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 0, 0], [1, 1, 1], [1, 1, 1]]))
print(solution([[1, 1], [1, 0]], [[0, 0], [1, 1]]))

