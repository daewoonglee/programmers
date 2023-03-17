from math import sqrt, pow


def solution(m, n, startX, startY, balls):
    # # 0.447742012
    # def calc_pts(x, y):
    #     X, Y = (startX*y), (x*startY)
    #     a = (X + Y - (startX*n) - (x*n)) / (y+startY-2*n)
    #     b = (X + Y) / (startX + x)
    #     c = (X + Y - (y*m) - (startY*m)) / (startX+x-2*m)
    #     d = (X + Y) / (y + startY)
    #
    #     return [[a,n], [0,b], [m,c], [d,0]] # URLD
    #
    # def calc_dist(x1, y1, x2, y2):
    #     return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
    #
    # ans = []
    # for targetX, targetY in balls:
    #     pts = calc_pts(targetX, targetY)
    #     if targetY == startY:
    #         pts.pop(1 if targetX < startX else 2)
    #     elif startX == targetX:
    #         pts.pop(0 if startY < targetY else 3)
    #     ans.append(min(
    #         [round(pow(calc_dist(startX, startY, px, py) + calc_dist(targetX, targetY, px, py), 2)) for px, py in pts]
    #     ))
    # return ans

    # code refactoring - 0.22795810100000002
    # MxN을 넓혀서 한번에 계산하는 방식, dist(startXY, pts) + dist(pts, targetXY) X, dist(startXY_expand, targetXY)
    ans = []
    pts = [(startX, 2*n-startY), (2*m-startX, startY), (-startX, startY), (startX, -startY)] # URLD
    for targetX, targetY in balls:
        if startY == targetY:
            new_pts = [pts[0], pts[1], pts[3]] if startX > targetX else [pts[0], pts[2], pts[3]]
        elif startX == targetX:
            new_pts = pts[:-1] if startY > targetY else pts[1:]
        else:
            new_pts = pts
        ans.append(min(list(map(lambda t: (targetX - t[0])**2 + (targetY - t[1])**2, new_pts))))
    return ans


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])) # [52, 37, 116]
print(solution(10, 10, 2, 7, [[3, 7]])) # [25]
print(solution(10, 10, 7, 2, [[7, 3]])) # [25]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]],
        [10, 10, 2, 7, [[3, 7]]],
        [10, 10, 7, 2, [[7, 3]]],
        [1000, 1000, 500, 500, [[2,1000], [1000,2], [999, 999]]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
