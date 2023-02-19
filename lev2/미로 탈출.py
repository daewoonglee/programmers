from collections import deque


def solution(maps):
    # code refactoring - 1.577800685
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

            visited[i][j] = 1
            for dx, dy in direction:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny] and maps[nx][ny] != "X":
                    q.append([nx, ny, cnt+1])

        return -1, -1, -1

    ROWS = len(maps)
    COLS = len(maps[0])
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    x, y = find_start_loc()
    lever_queue = deque([[x, y, 0]])
    Lx, Ly, Lcnt = search_maze(lever_queue, target="L")
    if Lcnt == -1: return -1

    exit_queue = deque([[Lx, Ly, 0]])
    Ex, Ey, Ecnt = search_maze(exit_queue, target="E")
    if Ecnt == -1: return -1

    return Lcnt + Ecnt


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
print(solution(["SOOOL","OOOOO","OOOOO","OOOOO","OOOOE"])) # 8
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOXE"])) # -1
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]],
        [["SOOOL","OOOOO","OOOOO","OOOOO","OOOOE"]],
        [["SOOOL","XXXXO","OOOOO","OXXXX","OOOXE"]],
        [["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]],
        [["SOOOL","XXXXO","OOOOO","OXXXX","OOOOO","XXXXO","OOOOO","OXXXX","OOOOO","XXXXO","OOOOE"]],
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
