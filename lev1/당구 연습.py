from math import sqrt, pow


def solution(m, n, startX, startY, balls):
    def calc_pts(x, y):
        a = ((startX*y) + (x*startY) - (startX*n) - (x*n)) / (y+startY-2*n)
        b = ((startX*y) + (x*startY)) / (startX + x)
        c = ((startX*y) + (x*startY) - (y*m) - (startY*m)) / (startX+x-2*m)
        d = ((startX*y) + (x*startY)) / (y + startY)

        return [[a,n], [0,b], [m,c], [d,0]]

    def calc_dist(x1, y1, x2, y2):
        return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

    ans = []
    for targetX, targetY in balls:
        pts = calc_pts(targetX, targetY)
        dist = []
        for px, py in pts:
            if px == startX == targetX or py == startY == targetY:
                continue
            dist.append(round(pow(calc_dist(startX, startY, px, py) + calc_dist(targetX, targetY, px, py), 2)))
        ans.append(min(dist))
    return ans

"""
10x10
(3,7), (7,7) -> (5,10)
4+9, 4+9 = 26
(sqrt(13)+sqrt(13))^2

(2,7), (3,7) -> (2.5,10)
(2.5-2)+(7-10) | (2.5-3)+(7-10)
sqrt(9.25) + sqrt(9.25)
(2sqrt(9.25))^2

(3,7), (7,3) -> (0,5.8)
(3-0)+(7-5.8) + (7-0)+(3-5.8)
9+1.44 + 49+7.84
(sqrt(10.44)+sqrt(56.84))^2
"""


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])) # [52, 37, 116]
