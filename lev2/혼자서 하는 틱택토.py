def solution(board):
    def cnt_OX(target):
        return sum([row.count(target) for row in board])

    def check_O():
        width = [(0,0),(1,0),(2,0)]
        height = [(0,0),(0,1),(0,2)]
        diagonal = [(0,0),(0,2)]

        for i, pts in enumerate([width, height, diagonal]):
            for x, y in pts:
                nx, ny = x, y
                for _ in range(3):
                    if board[nx][ny] != "O":
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

        # for x, y in width:
        #     for i in range(2):
        #         if board[x][y+i+1] != "O":
        #             break
        #     else:
        #         return 1
        #
        # for x, y in height:
        #     for i in range(2):
        #         if board[x+i+1][y] != "O":
        #             break
        #     else:
        #         return 1
        #
        # for x, y in diagonal:
        #     ny = 1 if y == 0 else -1
        #     for _ in range(2):
        #         x += 1
        #         y += ny
        #         if board[x][y] != "O":
        #             break
        #     else:
        #         return 1

    cnt_O = cnt_OX("O")
    cnt_X = cnt_OX("X")
    print(f"O: {cnt_O}, X: {cnt_X}")

    if cnt_O == cnt_X+1:
        return 1
    elif cnt_O == cnt_X:
        return 0 if check_O() else 1
    else:
        return 0


"""
if O==X+1  1
elif O==X
    if OOO -> 0 O가 선공이라 이후 X가 한번 더 진행했다는 의미 
    elif XXX -> 1 
else -1
"""
"O.X"   "OOO"   "..."   "O.O"   "O.O"   "OOX"   "X.X"
".O."   "..."   ".X."   "XOX"   "XOX"   "XXO"   ".O."
"..X"   "XXX"   "..."   "XXO"   "X.O"   "..."   "OXO"

# print(solution(["O.X", ".O.", "..X"])) # 1
# print(solution(["OOO", "...", "XXX"])) # 0
# print(solution(["...", ".X.", "..."])) # 0
# print(solution(["X.X", ".O.", "OXO"])) # 1
# print(solution(["...", "...", "..."])) # 1
# print(solution(["O.O", "XOX", "XXO"])) # 0
print(solution(["O.O", "XOX", "X.O"])) # 1
print(solution(["OOX", "XXO", "..."])) # 1
