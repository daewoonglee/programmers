from itertools import combinations
def solution(line):
    # 0.516930571058765
    #pts = []
    #for i in range(len(line)):
    #    for r in line[i:]:
    #        a, b, e = line[i]
    #        c, d, f = r
    #        denominator = (a*d-b*c)
    #        if not denominator: continue
    #        x = (b*f - e*d) / denominator
    #        y = (e*c - a*f) / denominator
    #        if x.is_integer() and y.is_integer():
    #            pts.append([int(x), int(y)])
   
    #min_x = min([p[0] for p in pts]) 
    #max_y = max([p[1] for p in pts])

    #w = max([p[0] for p in pts]) - min_x + 1
    #h = max_y - min([p[1] for p in pts]) + 1
    #ans = [["."] * w for _ in range(h)]

    #for p in pts:
    #    x = p[0] - min_x
    #    y = max_y - p[1]
    #    ans[y][x] = "*"

    #return ["".join(a) for a in ans]

    # code refactoring - 0.4543103240430355
    ans = []
    pts = set()
    for r1, r2 in combinations(line, 2):
        a, b, e = r1
        c, d, f = r2
        denominator = a*d-b*c
        if not denominator: continue
        x, y = (b*f-e*d)/denominator, (e*c-a*f)/denominator
        if x.is_integer() and y.is_integer():
            pts.add((int(x), int(y)))
    rx, ry = [[min(yx), max(yx)] for yx in list(zip(*pts))]
    ans = [['.']*(rx[1]-rx[0]+1) for _ in range(ry[1]-ry[0]+1)]
    for x, y in pts:
        ans[ry[1]-y][x-rx[0]] = "*"
    return ["".join(a) for a in ans]


#print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
#print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
#print(solution([[1, -1, 0], [2, -1, 0]]))
#print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
#print(solution([[1,0,-1], [0,1,-1]]))
#print(solution([[1,0,1,], [0,1,1]]))
#print(solution([[1,0,3],[0,1,3],[0,1,-3]]))
print(solution([[1,1,0],[-1,1,-4],[-1,1,-2],[-1,1,2]]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]], [[0, 1, -1], [1, 0, -1], [1, 0, 1]], [[1, -1, 0], [2, -1, 0]], [[1, -1, 0], [2, -1, 0], [4, -1, 0]], [[1,0,-1], [0,1,-1]], [[1,0,1,], [0,1,1]], [[1,0,3],[0,1,3],[0,1,-3]], [[1,1,0],[-1,1,-4],[-1,1,-2],[-1,1,2]]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

