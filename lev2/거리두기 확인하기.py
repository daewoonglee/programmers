from itertools import combinations


def solution(places):
    ans = []
    fail = ["O", "P"]
    for place in places:
        pts = []
        for i, p_line in enumerate(place):
            for j, p in enumerate(p_line):
                if p == "P": pts.append([i, j])

        dist = []
        for c in (list(combinations(pts, 2))):
            if abs(c[0][0]-c[1][0]) + abs(c[0][1]-c[1][1]) <= 2:
                dist.append(c)

        for d in dist:
            (x1, y1), (x2, y2) = d
            if x1 == x2:
                if abs(y2-y1) < 2 or (abs(y2-y1) == 2 and place[x1][y1+1] in fail):
                    ans.append(0)
                    break
            elif x1 < x2:
                if abs(x2-x1) <= 2 and (abs(y2-y1) == 1 and place[x1][y2] in fail or place[x1+1][y1] in fail):
                    ans.append(0)
                    break
        else: ans.append(1)
    return ans


# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# print(solution([["XXXXX", "XXXXX", "XXXXP", "XXXXP", "XXXXP"]])) # 0
# print(solution([["XXXXX", "XXXXX", "XXPPO", "XXXXX", "XXXXX"]])) # 0
# print(solution([["OOPOO", "OOOPO", "OOOOP", "OOOOO", "OOOOO"]])) # 0
print(solution([["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]])) # 0

