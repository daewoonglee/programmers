import sys
sys.setrecursionlimit(250000)


def solution(a, edges):
    def search(node, visited):
        visited[node] = 1
        cnt = 0
        for n in relation[node]:
            if visited[n]: continue
            c = search(n, visited)
            a[node] += a[n]
            cnt += (abs(a[n]) + c)
            a[n] = 0
        return cnt

    relation = {}
    for e in edges:
        l, r = e
        if l not in relation: relation[l] = []
        if r not in relation: relation[r] = []
        relation[l].append(r)
        relation[r].append(l)

    c = search(edges[0][0], [0 for _ in a])
    return c


# print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
# print(solution([0,-5,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 14
# print(solution([-3,-2,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 11
# print(solution([0,-1,2,1,2,-2,-2], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 18
# print(solution([0,0,0,0,0,0,0], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 0
print(solution([1,2,2,0,-1,-2,-2], [[0,1],[0,2],[0,3],[3,4],[4,5],[4,6]])) # 18
# print(solution([0,1,0], [[0,1], [1,2]])) # -1
