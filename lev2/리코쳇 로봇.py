from collections import deque


def solution(board):
    def get_start_points(target):
        pts = []
        for i, rows in enumerate(board):
            for j, r in enumerate(rows):
                if r == target:
                    pts = [i, j]
                    break
        return pts

    def move_robot(x, y, move_type):
        move_type = move_type.upper()
        if move_type == "U":
            while x > 0 and board[x-1][y] != "D":
                x -= 1
        elif move_type == "D":
            while ROW-1 > x and board[x+1][y] != "D":
                x += 1
        elif move_type == "L":
            while y > 0 and board[x][y-1] != "D":
                y -= 1
        elif move_type == "R":
            while y < COL-1 and board[x][y+1] != "D":
                y += 1
        return x, y

    def bfs(q, visited):
        while q:
            x, y, dep = q.popleft()
            # print(f" xy: {x}, {y}, depth: {dep}")
            for m in ["U", "D", "L", "R"]:
                nx, ny = move_robot(x, y, m)
                if board[nx][ny] == "G":
                    return dep+1
                # 1.5365211840000002
                # elif visited[nx][ny]:
                #     continue
                # else:
                #     visited[nx][ny] = 1

                # code refactoring - 1.469149224
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny, dep+1])
        return -1

    ROW, COL = len(board), len(board[0])
    start = get_start_points("R")
    visited_list = [[0] * COL for _ in range(ROW)]
    visited_list[start[0]][start[1]] = 1
    return bfs(deque([[*start, 0]]), visited_list)


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])) # 7
print(solution([".D.R", "....", ".G..", "...D"])) # -1
print(solution(["..D.R..", ".......", ".......", "D..DD.D", "......G"])) # 6
print(solution([".G.", "...", "..R"])) # -1
print(solution(["DG.", "...", "..R"])) # 2


if __name__ == "__main__":
    from timeit import Timer
    query = [
        ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."],
        [".D.R", "....", ".G..", "...D"],
        ["..D.R..", ".......", ".......", "D..DD.D", "......G"],
        [".G.", "...", "..R"],
        ["DG.", "...", "..R"],
        ["........R", ".........", ".........", ".........", ".........", "D........", "GDDDDDDDD"]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
