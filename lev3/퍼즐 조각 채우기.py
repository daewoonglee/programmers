def get_coords(board, n):
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
    # maps = [[1 if r else 0 for r in row] for row in board]
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                coords.append(dfs(i, j))
    return coords


def solution(game_board, table):
    g_coords = get_coords(game_board, 0)
    for gc in g_coords:
        print(gc)
    print()
    t_coords = get_coords(table, 1)
    for tc in t_coords:
        print(tc)
    print()

"""
퍼즐 형상에 대한 1차원 좌표값 변환 함수 작성 O

구현 필요 요소
1. 좌표값을 (0,0)으로 고정한 뒤 비교 좌표값을 상하좌우 회전하며 같은지 매칭 
    1-1. 매칭이 된다면 그에 상응하는 퍼즐 크기를 정답 변수에 추가 & 매칭된 비교군의 퍼즐 좌표값 제거 (중복 비교 없애기 위해)
    1-2. 매칭이 안된다면 비교군 중 아직 비교하지 않은 퍼즐에 대해 상하좌우 반복 비교
"""

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])) # 14
