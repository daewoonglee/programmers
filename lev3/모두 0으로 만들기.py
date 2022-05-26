def solution(a, edges):
    def search(node, visited):
        visited[node] = 1
        total, cnt = 0, 0
        for n in relation[node]:
            if visited[n]: continue
            t, c = search(n, visited)
            total += (t + a[n])
            cnt += (abs(a[n]) + c + c)
        return total, cnt

    relation = {}
    for e in edges:
        l, r = e
        if l not in relation: relation[l] = []
        if r not in relation: relation[r] = []
        relation[l].append(r)
        relation[r].append(l)
    print(relation)

    t, c = search(edges[0][0], [0 for _ in a])
    print(f"t: {t}, sum: {t + a[edges[0][0]]}, c: {c}")
    return c if t + a[edges[0][0]] == 0 else -1


# print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
# print(solution([0,-5,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 14
# print(solution([-3,-2,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 11
print(solution([0,-1,2,1,2,-2,-2], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 18
# print(solution([0,1,0], [[0,1], [1,2]])) # -1
