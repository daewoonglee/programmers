from collections import deque


def solution(maps):
    def find_start_loc():
        for i, row in enumerate(maps):
            for j, col in enumerate(row):
                if col == "S":
                    return i, j
        return -1, -1 # S가 존재하지 않는다면, 문제에서 해당 경우 X

    def search_maze(q, target):
        visited = [[0]*COLS for _ in range(ROWS)]
        while q:
            i, j, cnt = q.popleft()
            if maps[i][j] == target:
                return i, j, cnt
            elif visited[i][j] or maps[i][j] == "X":
                continue

            visited[i][j] = 1

            if i+1 < ROWS:
                q.append([i+1, j, cnt+1])
            if i-1 >= 0:
                q.append([i-1, j, cnt+1])
            if j+1 < COLS:
                q.append([i, j+1, cnt+1])
            if j-1 >= 0:
                q.append([i, j-1, cnt+1])

        return -1, -1, -1

    ROWS = len(maps)
    COLS = len(maps[0])

    x, y = find_start_loc()
    lever_queue = deque([[x, y, 0]])
    Lx, Ly, Lcnt = search_maze(lever_queue, target="L")
    if Lcnt == -1: return -1

    exit_queue = deque([[Lx, Ly, 0]])
    Ex, Ey, Ecnt = search_maze(exit_queue, target="E")
    if Ecnt == -1: return -1

    return Lcnt + Ecnt


"""
Find S -> Find L -> Find E

S 위치에서 L을 bfs로 탐색, L을 찾으면 그게 L의 최단 경로, 이외 찾던 경로 모두 리셋
-> 찾지 못하면 -1 반환
L 위치에서 E를 bfs로 탐색, E을 찾으면 그게 E의 최단 경로, 이외 찾던 경로 모두 리셋
-> 찾지 못하면 -1 반환

S O O O L
X X X X O
O O O O O
O X X X X
O O O O E 16

S O O O L
O O O O O
O O O O O
O O O O O
O O O O E 8

S O O O L
X X X X O
O O O O O
O X X X X
O O O X E -1
"""

# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
# print(solution(["SOOOL","OOOOO","OOOOO","OOOOO","OOOOE"])) # 8
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOXE"])) # -1
# print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1
