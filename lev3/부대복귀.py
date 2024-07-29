import sys
sys.setrecursionlimit(500000)


def solution(n, roads, sources, destination):
    def bfs(queue, depth):
        next_queue = []
        # 방문한 노드 갱신
        for cur_node in queue:
            visited[cur_node] = 1
            lookup_table[cur_node] = depth

        # 방문할 노드 탐색
        for cur_node in queue:
            for next_node in road_dict[cur_node]:
                if not visited[next_node]:
                    next_queue.append(next_node)

        if next_queue:
            bfs(next_queue, depth+1)

    # node 별 edge 연결
    road_dict = dict()
    for a, b in roads:
        if a not in road_dict:
            road_dict[a] = list()
        if b not in road_dict:
            road_dict[b] = list()
        road_dict[a].append(b)
        road_dict[b].append(a)

    # 0 indexing 맞추기 위해서 n+1
    lookup_table = [-1]*(n+1)
    visited = [0]*(n+1)
    lookup_table[destination] = 0 # 자기자신 0
    visited[destination] = 1
    bfs(road_dict[destination], 1)

    return [lookup_table[source] for source in sources]


# print(solution(3, [[1, 2], [2, 3]], [2, 3], 1)) # [1,2]
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)) # [2,-1,0]
print(solution(6, [[1, 2],[1, 3],[1,5],[5,4],[2,3],[3,5]], [1,2,3,4,5], 1)) # [0,1,1,2,1]
