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

    def search1(node, visited):
        visited[node] = 1
        cnt = a[node]
        for n in relation[node]:
            if visited[n]: continue
            cnt += search1(n, visited)
        ans[0] += abs(cnt)
        return cnt

    # search1
    ans = [0]
    if sum(a): return -1

    relation = {}
    for e in edges:
        l, r = e
        if l not in relation: relation[l] = []
        if r not in relation: relation[r] = []
        relation[l].append(r)
        relation[r].append(l)

    # 0.41819209700000004
    # c = search(edges[0][0], [0 for _ in a])
    # return c

    # code refactoring - 0.39843556199999997
    search1(edges[0][0], [0 for _ in a])
    return ans[0]


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
# print(solution([0,-5,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 14
# print(solution([-3,-2,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 11
# print(solution([0,-1,2,1,2,-2,-2], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 18
# print(solution([0,0,0,0,0,0,0], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]])) # 0
# print(solution([1,2,2,0,-1,-2,-2], [[0,1],[0,2],[0,3],[3,4],[4,5],[4,6]])) # 18
# print(solution([0,1,0], [[0,1], [1,2]])) # -1


if __name__ == "__main__":
    from timeit import Timer
    query = [[[-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]],
             [[0,-5,2,1,2], [[0,1],[3,4],[2,3],[0,3]]],
             [[-3,-2,2,1,2], [[0,1],[3,4],[2,3],[0,3]]],
             [[0,-1,2,1,2,-2,-2], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]]],
             [[0,0,0,0,0,0,0], [[0,1],[3,4],[2,3],[0,3],[5,1],[6,1]]],
             [[1,2,2,0,-1,-2,-2], [[0,1],[0,2],[0,3],[3,4],[4,5],[4,6]]],
             [[0,1,0], [[0,1], [1,2]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
