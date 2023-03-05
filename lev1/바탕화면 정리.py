def solution(wallpaper):
    # # 0.629445131
    # ans = [51, 51, -1, -1]
    # for i, rows in enumerate(wallpaper):
    #     for j, r in enumerate(rows):
    #         if r == "#":
    #             if ans[0] > i: ans[0] = i
    #             if ans[1] > j: ans[1] = j
    #             if ans[2] < i+1: ans[2] = i+1
    #             if ans[3] < j+1: ans[3] = j+1
    # return ans

    # code refactoring - 0.5012737780000001
    x, y = [], []
    for i, rows in enumerate(wallpaper):
        for j, r in enumerate(rows):
            if r == "#":
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x) + 1, max(y) + 1]


# print(solution([".#...", "..#..", "...#."])) # [0, 1, 3, 4]
# print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])) # [1, 3, 5, 8]
# print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])) # [0, 0, 7, 9]
print(solution(["..", "#."])) # [1, 0, 2, 1]
print(solution("#")) # [0, 0, 1, 1]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [".#...", "..#..", "...#."],
        ["..........", ".....#....", "......##..", "...##.....", "....#....."],
        [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."],
        ["..", "#."],
        ["#"],
        ["##################################################"*50],
        ["...#..................#.........." * 10]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))
