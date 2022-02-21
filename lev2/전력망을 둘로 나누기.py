def solution(n, wires):
    ans = n
    wires = [[w[0]-1,w[1]-1] for w in wires]
    wires.sort(key=lambda x: [x[0], x[1]])
    print(wires)
    g1, g2 = [0] * n, [0] * n
    for i in range(n-1):
        g1[wires[i][1]] = 1
        for j, wire in enumerate(wires):
            if i == j: continue
            l, r = wire
            if g1[l] or g1[r]:
                g1[l] = 1
                g1[r] = 1
            else:
                g2[l] = 1
                g2[r] = 1
        diff = abs(len([g for g in g1 if g]) - len([g for g in g2 if g]))
        g1, g2 = [0] * n, [0] * n
        if ans > diff:
            ans = diff
    return ans


#print(solution(3, [[1,2],[2,3]]))
#print(solution(7, [[1,2],[1,7],[2,3],[2,6],[3,4],[3,5]])) 
#print(solution(7, [[1,2],[1,5],[2,3],[2,6],[3,4],[3,7]]))
print(solution(7, [[1,2],[1,5],[2,3],[2,6],[5,8],[5,9]]))

