def solution(edges):
    """
    도넛: 정점 n, 간선 n
    막대: 정점 n, 간선 n-1
    8자: 정점 n, 간선 n+1
    """
    def dfs(cur_node, visited_node, edge_cnt):
        # 방문할 수 있는 노드가 없는 경우(빈 리스트)
        if cur_node not in edge_dict:
            visited_node.append("NONE")
            return visited_node, edge_cnt
        # 노드 방문하며 서치
        for i, next_node in enumerate(edge_dict[cur_node]):
            if not edge_flag[cur_node][i]:
                if cur_node not in visited_node:
                    visited_node.append(cur_node)
                edge_flag[cur_node][i] = True
                visited_node, edge_cnt = dfs(next_node, visited_node, edge_cnt+1)
        return visited_node, edge_cnt

    # edge 별 방문 리스트 생성
    edge_dict = dict()
    edge_flag = dict()
    for a, b in edges:
        if a not in edge_dict:
            edge_dict[a] = []
            edge_flag[a] = []
        edge_dict[a].append(b)
        edge_flag[a].append(False)
    # print(edge_dict)

    # 무관한 정점에서 edge dfs로 방문
    ans = [edges[0][0], 0, 0, 0]
    for n in edge_dict[edges[0][0]]:
        node, edge = dfs(n, [], 0)
        # print(f"n: {n}, node cnt: {node}, edge cnt: {edge}")
        if len(node) == edge: ans[1] += 1 # 도넛
        elif len(node)-1 == edge: ans[2] += 1 # 막대
        else: ans[3] += 1 # 8자
    return ans


# print(solution([[2, 3], [4, 3], [1, 1], [2, 1]])) # [2, 1, 1, 0]
# print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])) # [4, 0, 1, 2]
print(solution([[1,4], [3,2],[4,3],[5,4],[6,5],[4,6],[2,4],
                [7,8],[8,9],[9,8],[8,7],[1,9],
                [10,11],[11,13],[13,15],[15,16],[16,14],[14,13],[13,12],[12,10],[1,16],
                [17,18],[18,19],[19,20],[20,21], [1,21],
                [22,24],[24,26],[26,27],[27,29],[29,30],[30,28],[28,26],[26,25],[25,23],[23,22], [1,30],
                [36,31],[31,32],[32,33],[33,34],[34,35],[35,36], [1,36]])) # [2, 1, 0, 0]
print(solution([[2, 1], [1, 3], [2, 4], [4, 5], [2, 6], [6, 7]]))


