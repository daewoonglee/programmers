"""
문제 설명
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다.
예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항
섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고,
costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다.
즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.

입출력 예
n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4

입출력 예 설명
costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.
image.png
"""


def visited(graphs, visited_list, k=0, move=0):
    visited_list[k] = 0
    if not sum(visited_list):
        return move

    min_idx = 101
    for i, node in enumerate(graphs[k]):
        if node and min_idx > node:
            min_idx = i

    print(f"graphs: {graphs}")
    print(f"k: {k}, min: {min_idx}, graph: {graphs[min_idx]}, move: {move}\n")
    move += graphs[k][min_idx]
    graphs[k][min_idx] = 0
    graphs[min_idx][k] = 0
    return visited(graphs, visited_list, min_idx, move)


def solution(n, costs):
    graphs = {i: [0 for _ in range(n)] for i in range(n)}
    for cost in costs:
        i, j, c = cost
        graphs[i][j] = c
        graphs[j][i] = c
    visited_list = [1 for _ in range(n)]
    return visited(graphs, visited_list)


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
