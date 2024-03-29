"""
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
입출력 예 설명
예제 #1
아래와 같이 2개의 네트워크가 있습니다.
image0.png

예제 #2
아래와 같이 1개의 네트워크가 있습니다.
image1.png
"""


def solution(n, computers):
    # 0.32934670499999996
    # ans = 0
    # stack = []
    # visited = []
    # idx = 0
    # while len(visited) != n:
    #     for j, c in enumerate(computers[idx]):
    #         if idx != j and c:
    #             if j not in visited:
    #                 if not stack or j not in stack:
    #                     stack.append(j)
    #     visited.append(idx)
    #     if not stack:
    #         ans += 1
    #         for i in range(n):
    #             if i not in visited:
    #                 idx = i
    #                 break
    #     else:
    #         idx = stack.pop(0)
    # return ans

    # code refactoring - 0.224537
    def visit(idx, visited, computers):
        visited[idx] = 1
        for j, com in enumerate(computers[idx]):
            if not visited[j] and com:
                visit(j, visited, computers)

    visited = [0] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            visit(i, visited, computers)
            ans += 1
    return ans


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1
# print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]]))   # 3
# print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 1]]))   # 3
# print(solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))   # 1
# print(solution(5, [[1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 1, 1]]))   # 1
# print(solution(5, [[1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1]]))   # 2
print(solution(5, [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))   # 1


if __name__ == '__main__':
    from timeit import Timer
    query = [[3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
             [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
             [5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]]],
             [5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 1]]],
             [3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]],
             [5, [[1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 1, 1]]],
             [5, [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
