def solution(board):
    def cnt_OX(target):
        return sum([row.count(target) for row in board])

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

    cnt_O = cnt_OX("O")
    cnt_X = cnt_OX("X")
    if cnt_O == cnt_X+1:
        return 0 if check_OX("X") else 1
    elif cnt_O == cnt_X:
        return 0 if check_OX("O") else 1
    else:
        return 0


"""
if O==X+1  1
elif O==X
    if OOO -> 0 O가 선공이라 이후 X가 한번 더 진행했다는 의미 
    elif XXX -> 1 
else -1
"""
"O.X"   "OOO"   "..."   "O.O"   "O.O"   "OOX"   "XOX"
".O."   "..."   ".X."   "XOX"   "XOX"   "XXO"   "OOX"
"..X"   "XXX"   "..."   "XXO"   "X.O"   "..."   "OOX"

# print(solution(["O.X", ".O.", "..X"])) # 1
# print(solution(["OOO", "...", "XXX"])) # 0
# print(solution(["...", ".X.", "..."])) # 0
# print(solution(["X.X", ".O.", "OXO"])) # 1
# print(solution(["...", "...", "..."])) # 1
# print(solution(["O.O", "XOX", "XXO"])) # 0
# print(solution(["O.O", "XOX", "X.O"])) # 1
# print(solution(["OOX", "XXO", "..."])) # 1
print(solution(["XOX", "OOX", "OOX"])) # 0
