def solution(wallpaper):
    ans = [51, 51, -1, -1]
    for i, rows in enumerate(wallpaper):
        for j, r in enumerate(rows):
            if r == "#":
                if ans[0] > i: ans[0] = i
                if ans[1] > j: ans[1] = j
                if ans[2] < i+1: ans[2] = i+1
                if ans[3] < j+1: ans[3] = j+1
    return ans


"""
반드시 하나 이상의 파일이 존재
#을 서치하면 min x,y, max x,y를 찾으면 그게 최단 거리
맨위# minx, 맨아# maxx, 맨왼# miny, 맨오# maxy, 
"""


# print(solution([".#...", "..#..", "...#."])) # [0, 1, 3, 4]
# print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])) # [1, 3, 5, 8]
# print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])) # [0, 0, 7, 9]
print(solution(["..", "#."])) # [1, 0, 2, 1]
