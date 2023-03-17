from math import sqrt, pow


def solution(m, n, startX, startY, balls):
    def calc_pts(x, y):
        X, Y = (startX*y), (x*startY)
        a = (X + Y - (startX*n) - (x*n)) / (y+startY-2*n)
        b = (X + Y) / (startX + x)
        c = (X + Y - (y*m) - (startY*m)) / (startX+x-2*m)
        d = (X + Y) / (y + startY)

        return [[a,n], [0,b], [m,c], [d,0]] # URLD

    def calc_dist(x1, y1, x2, y2):
        return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

    ans = []
    for targetX, targetY in balls:
        pts = calc_pts(targetX, targetY)
        if targetY == startY:
            pts.pop(1 if targetX < startX else 2)
        elif startX == targetX:
            pts.pop(0 if startY < targetY else 3)

        dist = []
        for px, py in pts:
            dist.append(round(pow(calc_dist(startX, startY, px, py) + calc_dist(targetX, targetY, px, py), 2)))
        ans.append(min(dist))
    return ans


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])) # [52, 37, 116]
print(solution(10, 10, 2, 7, [[3, 7]])) # [25]
print(solution(10, 10, 7, 2, [[7, 3]])) # [25]

