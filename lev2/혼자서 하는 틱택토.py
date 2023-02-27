def solution(board):
    # def cnt_OX(target):
        # 0.414120274
        # return sum([row.count(target) for row in board])

    def cnt_OX():
        # code refactoring - 0.323417551
        cnt_O = 0
        cnt_X = 0
        for row in board:
            for r in row:
                if r == 'O':
                    cnt_O += 1
                elif r == 'X':
                    cnt_X += 1
        return cnt_O, cnt_X

    def check_OX(target):
        width = [(0,0),(1,0),(2,0)]
        height = [(0,0),(0,1),(0,2)]
        diagonal = [(0,0),(0,2)]

        for i, pts in enumerate([width, height, diagonal]):
            for x, y in pts:
                nx, ny = x, y
                for _ in range(3):
                    if board[nx][ny] != target:
                        break

                    if i == 0:
                        ny += 1
                    elif i == 1:
                        nx += 1
                    else:
                        nx += 1
                        ny += 1 if y == 0 else -1
                else:
                    return 1

    # cnt_O, cnt_X = cnt_OX("O"), cnt_OX("X")
    cnt_O, cnt_X = cnt_OX()
    
    if cnt_O == cnt_X+1:
        return 0 if check_OX("X") else 1
    elif cnt_O == cnt_X:
        return 0 if check_OX("O") else 1
    else:
        return 0


# print(solution(["O.X", ".O.", "..X"])) # 1
# print(solution(["OOO", "...", "XXX"])) # 0
# print(solution(["...", ".X.", "..."])) # 0
# print(solution(["X.X", ".O.", "OXO"])) # 1
# print(solution(["...", "...", "..."])) # 1
# print(solution(["O.O", "XOX", "XXO"])) # 0
# print(solution(["O.O", "XOX", "X.O"])) # 1
# print(solution(["OOX", "XXO", "..."])) # 1
print(solution(["XOX", "OOX", "OOX"])) # 0


if __name__ == "__main__":
    from timeit import Timer
    query = [
        ["O.X", ".O.", "..X"],
        ["OOO", "...", "XXX"],
        ["...", ".X.", "..."],
        ["X.X", ".O.", "OXO"],
        ["...", "...", "..."],
        ["O.O", "XOX", "XXO"],
        ["O.O", "XOX", "X.O"],
        ["OOX", "XXO", "..."],
        ["XOX", "OOX", "OOX"]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
