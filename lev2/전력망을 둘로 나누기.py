def solution(n, wires):
    #ans = n
    #wires = [[w[0]-1,w[1]-1] for w in wires]
    #wires.sort(key=lambda x: [x[0], x[1]])
    #print(wires)
    #g1, g2 = [0] * n, [0] * n
    #for i in range(n-1):
    #    g1[wires[i][1]] = 1
    #    for j, wire in enumerate(wires):
    #        if i == j: continue
    #        l, r = wire
    #        if g1[l] or g1[r]:
    #            g1[l] = 1
    #            g1[r] = 1
    #        else:
    #            g2[l] = 1
    #            g2[r] = 1
    #    diff = abs(len([g for g in g1 if g]) - len([g for g in g2 if g]))
    #    g1, g2 = [0] * n, [0] * n
    #    if ans > diff:
    #        ans = diff
    #return ans

    from collections import Counter
    ans = n
    wires_1d = sum(wires, [])
    cnt_wires = Counter(wires_1d)
    max_edge = max(cnt_wires, key=cnt_wires.get)
    edge_idx = [i for i,w in enumerate(wires) if w[0] == max_edge or w[1] == max_edge]
    g1, g2 = set(), set()
    for i in edge_idx:
        g1.add(wires[i][0])
        g2.add(wires[i][1])
        for j in edge_idx:
            if i == j: continue
            if wires[j][0] in g1 or wires[j][1] in g1:
                g1.add(wires[j][0])
                g1.add(wires[j][1])
            else:
                g2.add(wires[j][0])
                g2.add(wires[j][1])

        for z, w in enumerate(wires):
            if z in edge_idx: continue
            if w[0] in g1 or w[1] in g1:
                g1.add(w[0])
                g1.add(w[1])
            else:
                g2.add(w[0])
                g2.add(w[1]) 

        diff = abs(len(g1) - len(g2))
        g1, g2 = set(), set()
        if ans > diff:
            ans = diff
    return ans

    

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
#print(solution(3, [[1,2],[2,3]]))
#print(solution(7, [[1,2],[1,7],[2,3],[2,6],[3,4],[3,5]])) 
#print(solution(7, [[1,2],[1,5],[2,3],[2,6],[3,4],[3,7]]))
#print(solution(3, [[1,10],[10,100]]))

