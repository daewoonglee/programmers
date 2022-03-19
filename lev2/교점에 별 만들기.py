def solution(line):
    pts = []
    for i in range(len(line)):
        for r in line[i:]:
            a, b, e = line[i]
            c, d, f = r
            denominator = (a*d-b*c)
            if not denominator: continue
            x = (b*f - e*d) / denominator
            y = (e*c - a*f) / denominator
            if x.is_integer() and y.is_integer():
                pts.append([int(x), int(y)])
   
    min_x = min([p[0] for p in pts]) 
    max_y = max([p[1] for p in pts])

    w = max([p[0] for p in pts]) - min_x + 1
    h = max_y - min([p[1] for p in pts]) + 1
    ans = [["."] * w for _ in range(h)]

    for p in pts:
        x = p[0] - min_x
        y = max_y - p[1]
        ans[y][x] = "*"

    return ["".join(a) for a in ans]


#print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
#print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
#print(solution([[1, -1, 0], [2, -1, 0]]))
#print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
#print(solution([[1,0,-1], [0,1,-1]]))
#print(solution([[1,0,1,], [0,1,1]]))
#print(solution([[1,0,3],[0,1,3],[0,1,-3]]))
print(solution([[1,1,0],[-1,1,-4],[-1,1,-2],[-1,1,2]]))

