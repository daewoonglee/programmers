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


def solution(n, costs):
    # 0.335299591
    # costs.sort(key=lambda x: x[-1], reverse=True)
    # ans = 0
    # paths = set([costs[-1][0]])
    # while len(paths) != n:
    #     for i in range(len(costs)-1, -1, -1):
    #         cost = costs[i]
    #         if cost[0] in paths and cost[1] in paths:
    #             continue
    #         if cost[0] in paths or cost[1] in paths:
    #             paths.update(cost[:2])
    #             ans += cost[-1]
    #             costs.pop(i)
    #             break
    # return ans

    # code refactoring - 0.29347300800000004
    ans = 0
    paths = 0
    cycle = {i: i for i in range(n)}
    costs.sort(key=lambda x: x[-1])
    for cost in costs:
        if cost[0] > cost[1]:
            cost[0], cost[1] = cost[1], cost[0]
        if cycle[cost[0]] == cycle[cost[1]]:
            continue
        ans += cost[-1]
        paths += 1
        past = cycle[cost[1]]
        cycle[cost[1]] = cycle[cost[0]]
        for k, v in cycle.items():
            if v == past:
                cycle[k] = cycle[cost[0]]
        if paths == n-1:
            break
    return ans


# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])) # 4
# print(solution(4, [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 2, 2], [2, 3, 2]])) # 3
# print(solution(5, [[1, 2, 3], [3, 4, 2], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [2, 3, 3]]))   # 4
# print(solution(4, [[0, 1, 1], [0, 2, 1], [1, 2, 1], [1, 3, 2], [2, 3, 3]])) # 4
# print(solution(5, [[0, 1, 1], [0, 2, 1], [1, 2, 1], [1, 3, 3], [3, 4, 1]])) # 6
# print(solution(5, [[0, 1, 3], [0, 2, 3], [0, 4, 1], [1, 2, 2], [1, 3, 2], [1, 4, 3], [2, 3, 2], [3, 4, 2]]))    # 7
# print(solution(4, [[0, 1, 1], [2, 3, 3], [1, 3, 2], [1, 2, 1], [0, 2, 1]])) # 4
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]])) # 9


if __name__ == '__main__':
    from timeit import Timer
    query = [[4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]],
             [4, [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 2, 2], [2, 3, 2]]],
             [5, [[1, 2, 3], [3, 4, 2], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [2, 3, 3]]],
             [4, [[0, 1, 1], [0, 2, 1], [1, 2, 1], [1, 3, 2], [2, 3, 3]]],
             [5, [[0, 1, 1], [0, 2, 1], [1, 2, 1], [1, 3, 3], [3, 4, 1]]],
             [5, [[0, 1, 3], [0, 2, 3], [0, 4, 1], [1, 2, 2], [1, 3, 2], [1, 4, 3], [2, 3, 3], [3, 4, 2]]],
             [4, [[0, 1, 1], [2, 3, 3], [1, 3, 2], [1, 2, 1], [0, 2, 1]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
