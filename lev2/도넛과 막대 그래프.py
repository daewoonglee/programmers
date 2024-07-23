import sys
sys.setrecursionlimit(499999)


def solution(edges):
    """
    도넛: 정점 n, 간선 n
    막대: 정점 n, 간선 n-1
    8자: 정점 n, 간선 n+1
    """
    def dfs(cur_node, node_cnt, edge_cnt):
        # 방문할 수 있는 노드가 없는 경우는 막대 그래프
        if cur_node not in edge_dict:
            return node_cnt, edge_cnt
        # 방출 간선이 2개면 8자 그래프
        elif len(edge_dict[cur_node]) == 2:
            print(f"88 cur: {cur_node}, cnt: {node_cnt}, {edge_cnt}")
            return node_cnt, edge_cnt+2

        # 노드 방문하며 서치
        if not edge_flag[cur_node][0]:
            edge_flag[cur_node][0] = True
            node_cnt, edge_cnt = dfs(edge_dict[cur_node][0], node_cnt+1, edge_cnt+1)
        # 이미 방문한 노드 재방문 -> 도넛
        else: edge_cnt += 1

        return node_cnt, edge_cnt

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

    # 무관한 정점 서치
    max_len = max(len(v) for v in edge_dict.values())
    max_keys = [k for k, v in edge_dict.items() if len(v) == max_len]
    all_values = [v for values in edge_dict.values() for v in values]
    random_node_key = [k for k in max_keys if k not in all_values][0]

    # 무관한 정점에서 edge dfs로 방문, 무관한 정점은 edge가 가장 많은 노드
    ans = [random_node_key, 0, 0, 0]
    for n in edge_dict[random_node_key]:
        node, edge = dfs(n, 1, 0)
        # print(f"n: {n}, node cnt: {node}, edge cnt: {edge}")
        if node == edge: ans[1] += 1 # 도넛
        elif node-1 == edge: ans[2] += 1 # 막대
        else: ans[3] += 1 # 8자
    return ans


# print(solution([[2, 3], [4, 3], [1, 1], [2, 1]])) # [2, 1, 1, 0]
# print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])) # [4, 0, 1, 2]
# print(solution([
#     [2,3],[3,4],[4,5],[5,1],[1,2], [7,2], # 도넛
#     [10,11],[11,12],[12,13],[13,14], [7,14], # 막대
#     [32,27],[27,31],[31,21],[21,32],[31,29],[29,26],[26,30],[30,31], [7,32] # 8자
# ]))
print(solution([[32,27],[27,31],[31,21],[21,32],[31,29],[29,26],[26,30],[30,31], [7,32],
                [7,100]])) # [7, 0, 1, 1]



