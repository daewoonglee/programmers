def get_puzzles(board, n):
    def trans_coord(puzzle_coords):
        puzzle_coords.sort(key=lambda x: [x[0], x[1]])
        min_x, min_y = puzzle_coords[0][0], min([pc[1] for pc in puzzle_coords])
        trans_puzzle_coords = [(pc[0]-min_x, pc[1]-min_y) for pc in puzzle_coords]
        return trans_puzzle_coords

    def dfs(x, y):
        puzzle = []
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if maps[x][y] == 0:
                puzzle.append((x, y))
                if x+1 < N: stack.append((x+1, y))
                if x-1 >= 0: stack.append((x-1, y))
                if y+1 < N: stack.append((x, y+1))
                if y-1 >= 0: stack.append((x, y-1))
                maps[x][y] = 1
        return puzzle

    N = len(board)
    maps = [[not n if r else n for r in row] for row in board]
    puzzles = [trans_coord(dfs(i, j)) for i in range(N) for j in range(N) if maps[i][j] == 0]
    return puzzles


def is_match(gp, tp, m, idx):
    def rotate(puzzle):
        H = max(p[0] for p in puzzle)
        rot_puzzle = [(p[1], abs(p[0]-H)) for p in puzzle]
        rot_puzzle.sort(key=lambda x: [x[0], x[1]])
        return rot_puzzle

    if m[idx] or len(gp) != len(tp): return False

    for i in range(4):
        for g, t in zip(gp, tp):
            if g != t: break
        else:
            m[idx] = 1
            return True
        tp = rotate(tp)
    return False


# 2.912573497
def solution(game_board, table):
    game_puzzles = get_puzzles(game_board, 0)
    table_puzzles = get_puzzles(table, 1)
    matching = [0 for _ in table_puzzles]
    ans = 0
    for game_puzzle in game_puzzles:
        for i, table_puzzle in enumerate(table_puzzles):
            if is_match(game_puzzle, table_puzzle, matching, i):
                ans += len(game_puzzle)
                break
    return ans


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
               [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])) # 14

# print(solution([[0,0,0],[0,0,0],[0,0,0]],
#                [[1,1,1],[1,1,1],[1,1,1]])) # 9

# print(solution([[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]],
#                [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,0,1]])) # 15


if __name__ == "__main__":
    from timeit import Timer
    query = [[[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
              [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]],
             [[[0,0,0],[0,0,0],[0,0,0]],
              [[1,1,1],[1,1,1],[1,1,1]]],
             [[[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]],
              [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,0,1]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

