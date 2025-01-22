def solution(mats, park):
    ans = -1
    N, M = len(park), len(park[0])
    dp_mats = [[0] * M for _ in range(N)]
    max_mat = 0
    for x in range(N):
        for y in range(M):
            if park[x][y] == "-1":
                dp_mats[x][y] = 1
                if x>0 and y>0:
                    dp_mats[x][y] = min(dp_mats[x - 1][y], dp_mats[x][y - 1], dp_mats[x - 1][y - 1]) + 1
                    max_mat = max_mat if max_mat > dp_mats[x][y] else dp_mats[x][y]
            else:
                dp_mats[x][y] = 0

    for m in mats:
        if ans < m <= max_mat:
            ans = m
    return ans



print(solution([5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]])) # 3
# print(solution([5,3,2], [["A"]])) # -1
# print(solution([1], [["-1"]])) # -1