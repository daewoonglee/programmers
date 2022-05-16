from collections import deque


def solution(n, edge):
    # 0.229496118
    # visited = [0 for _ in range(n)]
    # info = {}
    # for v in edge:
    #     if v[0] not in info:
    #         info[v[0]] = []
    #     if v[1] not in info:
    #         info[v[1]] = []
    #     info[v[0]].append(v[1])
    #     info[v[1]].append(v[0])
    #
    # q = deque(info[1])
    # visited[0] = 1
    # ans = 0
    # while len(q):
    #     N = len(q)
    #     ans = q.copy()
    #     for _ in range(N):
    #         node = q.popleft()
    #         if visited[node-1]: continue
    #         visited[node-1] = 1
    #         for v in info[node]:
    #             if not visited[v-1] and v not in q:
    #                 q.append(v)
    #
    # return len(set(ans))

    # code refactoring - 0.198095528
    visited = [0 for _ in range(n)]
    depth = [0 for _ in range(n)]
    info = [[] for _ in range(n)]
    for (a, b) in edge:
        info[a-1].append(b-1)
        info[b-1].append(a-1)

    q = deque([0])
    visited[0] = 1
    while len(q):
        node = q.popleft()
        for n in info[node]:
            if visited[n]: continue
            visited[n] = 1
            depth[n] = depth[node] + 1
            q.append(n)
    depth.sort()
    return depth.count(depth[-1])


# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [2, 1], [2, 4], [5, 2]]))
print(solution(6, [[2, 1], [1, 3], [3, 2], [4, 6], [4, 5], [2, 5]]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]], [6, [[3, 6], [4, 3], [3, 2], [1, 3], [2, 1], [2, 4], [5, 2]]], [6, [[2, 1], [1, 3], [3, 2], [4, 6], [4, 5], [2, 5]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
