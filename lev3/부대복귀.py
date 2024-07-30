from collections import deque


def solution(n, roads, sources, destination):
    # node 별 edge 연결
    road_path = [[] for _ in range(n+1)]
    for a, b in roads:
        road_path[a].append(b)
        road_path[b].append(a)

    lookup_table = [-1]*(n+1) # 0 indexing 맞추기 위해서 n+1
    lookup_table[destination] = 0 # 자기자신 0
    queue = deque([destination])
    while queue:
        cur_node = queue.popleft()
        depth = lookup_table[cur_node]
        for next_node in road_path[cur_node]:
            if lookup_table[next_node] == -1: # 방문하지 않은 노드
                lookup_table[next_node] = depth+1
                queue.append(next_node)
    return [lookup_table[source] for source in sources]


# print(solution(3, [[1, 2], [2, 3]], [2, 3], 1)) # [1,2]
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)) # [2,-1,0]
print(solution(6, [[1, 2],[1, 3],[1,5],[5,4],[2,3],[3,5]], [1,2,3,4,5], 1)) # [0,1,1,2,1]
