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

    print(f"pts: {pts}")
    
    max_x = max([p[0] for p in pts])
    max_y = max([p[1] for p in pts])

    w = max_x - min([p[0] for p in pts]) + 1
    h = max_y - min([p[1] for p in pts]) + 1
    ans = [["."] * w for _ in range(h)]

    # [[-2, 2], [-1, 1], [1, -1]]
    # maxx: 1, maxy: 2, w: 4, h: 4
    print(f"maxx: {max_x}, maxy: {max_y}, w: {w}, h: {h}")

#maxx: 1, maxy: 1, w: 3, h: 1
#p: [1, 1], x: 2, y:0 -> (2,0)
#p: [-1, 1], x: 1, y:0 -> (0,0)

    for p in pts:
        x = abs(p[0]) + max_x if p[0] < 0 else max_x - p[0]
        #x = p[0] + max_x if p[0] < 0 else max_x + p[0]
        y = abs(p[1]) + max_y if p[1] < 0 else max_y - p[1]
        print(f"p: {p}, x: {x}, y:{y}")
        ans[y][x] = "*"

    for r in ["".join(a) for a in ans]:
        print(r)

    return ["".join(a) for a in ans]


#print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
#print(solution([[1, -1, 0], [2, -1, 0]]))
#print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
#print(solution([[1,0,-1], [0,1,-1]]))
#print(solution([[1,0,1,], [0,1,1]]))
#print(solution([[1,0,3],[0,1,3],[0,1,-3]]))
print(solution([[1,1,0],[-1,1,-4],[-1,1,-2],[-1,1,2]]))

