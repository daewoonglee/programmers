def get_coords(board, n):
    def trans_coord(coord):
        coord.sort(key=lambda x: [x[0], x[1]])
        min_x = coord[0][0]
        min_y = min([c[1] for c in coord])
        t_coord = []
        for c in coord:
            t_coord.append((c[0]-min_x, c[1]-min_y))
        return t_coord

    def dfs(x, y):
        c = []
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if maps[x][y] == 0:
                c.append((x, y))
                if x+1 < N: stack.append((x+1, y))
                if x-1 >= 0: stack.append((x-1, y))
                if y+1 < N: stack.append((x, y+1))
                if y-1 >= 0: stack.append((x, y-1))
                maps[x][y] = 1
        return c

    N = len(board)
    coords = []
    maps = [[not n if r else n for r in row] for row in board]
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                coords.append(trans_coord(dfs(i, j)))
    return coords


def is_match(gc, tc, m, idx):
    def rotate(coord):
        r_coord = []
        for c in coord:
            x, y = c
            r_coord.append()
        return r_coord

    if m[idx]: return False
    for i in range(4):
        for g, t in zip(gc, tc):
            if g != t: break
        else:
            m[idx] = 1
            return True
        tc = rotate(tc)


def solution(game_board, table):
    g_coords = get_coords(game_board, 0)
    t_coords = get_coords(table, 1)

    matching = [0 for _ in t_coords]
    ans = 0
    for g_coord in g_coords:
        for i, t_coord in enumerate(t_coords):
            if is_match(g_coord, t_coord, matching, i):
                ans += len(g_coord)
                break
    return ans

"""
구현 필요 요소
1. 비교 좌표값을 상하좌우 회전하며 같은지 매칭
"""

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])) # 14
