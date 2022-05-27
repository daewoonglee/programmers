def solution(a, edges):
    def search(node, visited):
        visited[node] = 1
        total, cnt = 0, 0
        for n in relation[node]:
            if visited[n]: continue
            c = search(n, visited)
            a[node] += a[n]
            cnt += (abs(a[n]) + c)
            a[n] = 0
        return cnt

    # 1/2               5/-2
    #    \              /
    #    0/1 - 3/0 - 4/-1
    #    /              \
    # 2/2               6/-2
    #
    # [1,2,2,0,-1,-2,-2], [[0,1],[0,2],[0,3],[3,4],[4,5],[4,6]]

    # [3,0,2,0,-1,-2,-2], cnt=2,node=0,n=1
    # [5,0,0,0,-1,-2,-2], cnt=4,node=0,n=2
    # [5,0,0,0,-1,-2,-2], cnt=4,node=0,n=3

    # [5,0,0,0,-1,-2,-2], cnt=0,node=3,n=4,
    # [5,0,0,0,-3,0,-2], cnt=2,node=4,n=5
    # [5,0,0,0,-5,0,0], cnt=4,node=4,n=6
    # [5,0,0,-5,0,0,0], cnt=9,c=4,node=3,n=4

    # [0,0,0,0,0,0,0], cnt=18,node=0,n=3

    relation = {}
    for e in edges:
        l, r = e
        if l not in relation: relation[l] = []
        if r not in relation: relation[r] = []
        relation[l].append(r)
        relation[r].append(l)
    print(relation)

    c = search(edges[0][0], [0 for _ in a])
    # print(f"t: {t}, sum: {t + a[edges[0][0]]}, c: {c}")
    # return c if t + a[edges[0][0]] == 0 else -1
    return c if not sum(a) else -1


# print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
# print(solution([0,-5,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 14
# print(solution([-3,-2,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 11
# print(solution([0,-1,2,1,2,-2,-2], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 18
# print(solution([0,0,0,0,0,0,0], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 0
# print(solution([1,2,2,0,-1,-2,-2], [[0,1],[0,2],[0,3],[3,4],[4,5],[4,6]])) # 18
print(solution([0,1,0], [[0,1], [1,2]])) # -1

# 1/2               5/-2
#    \              /
#    0/1 - 3/0 - 4/-1
#    /              \
# 2/2               6/-2
