from collections import deque


def solution(storage, requests):
    def bfs(cnt):
        visited = [[0] * M for _ in range(N)]
        q = deque([[0, 0]])
        visited[0][0] = 1
        log = []
        while q:
            x, y = q.popleft()
            if warehouse[x][y] == request_query:
                log.append([x, y])
                cnt -= 1
            else:
                for mx, my in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= mx + x < N and 0 <= my + y < M and visited[mx + x][my + y] != 1:
                        if warehouse[mx + x][my + y] in [0, request_query]:
                            q.append([x + mx, y + my])
                            visited[mx + x][my + y] = 1
        for x, y in log:
            warehouse[x][y] = 0
        return cnt

    N, M = len(storage) + 2, len(storage[0]) + 2
    warehouse = [[0] * M for _ in range(N)]
    for i, s_row in enumerate(storage):
        for j, ch in enumerate(s_row):
            warehouse[i + 1][j + 1] = ch

    ans = (N - 2) * (M - 2)
    for request_query in requests:
        # 전체 탐색하며 삭제
        if len(request_query) == 2:
            query = request_query[0]
            for i in range(1, N-1):
                for j in range(1, M-1):
                    if warehouse[i][j] == query:
                        warehouse[i][j] = 0
                        ans -= 1
        # bfs 탐색
        else:
            ans = bfs(ans)
    return ans


# print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])) # 11
# print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"])) # 4
# print(solution(["CCCCCC", "CXZVXC", "CXCCCC"], ["XX","Z"]))
print(solution(["BBBB", "ACDE", "BBBB"], ["CC","D","A"])) # 9, 10