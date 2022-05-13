from collections import deque


def solution(n, edge):
    visited = [0 for _ in range(n)]
    vertex = sorted([[e[1], e[0]] if e[0] > e[1] else [*e] for e in edge])
    info = {}
    for v in vertex:
        if v[0] not in info:
            info[v[0]] = []
        info[v[0]].append(v[1])
    print(f"info {info}")
    print(f"vertex: {vertex}")
    print(f"visited: {visited}")

    q = deque()
    for v in info[1]:
        q.append(v)
    print(f"init q: {q}")
    ans = 0
    depth = 1
    while len(q):
        N = len(q)
        ans = q.copy()
        for _ in range(N):
            node = q.popleft()
            if visited[node-1]: continue
            visited[node-1] = 1
            if node in info:
                for v in info[node]:
                    if not visited[v-1] and v not in q:
                        q.append(v)

        depth += 1
        print(f"node: {node}, visited: {visited}, q: {q}")
    print(f"depth: {depth}")
    print(f"ans: {ans}")
    return len(set(ans))


# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [2, 1], [2, 4], [5, 2]]))
print(solution(5, [[1, 2], [1, 3], [3, 4]]))

#         1
#       /   \
#      2  -  3
#    /   \  /  \
#   5     4     6

# vertex 정렬 -> 1번 노드부터 탐색하기 위해
# bfs 방식으로 1번 노드에 연결된 간선을 queue에 저장
# queue를 돌면서 depth를 +1 씩 진행
# 마지막 depth에 해당하는 노드들의 수를 리턴
