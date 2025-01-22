def solution(mats, park):
    def is_empty(mat_x, mat_y, mat_size):
        for i in range(mat_size):
            for j in range(mat_size):
                if park[mat_x + i][mat_y + j] != "-1":
                    return False
        return True

    ans = -1
    N, M = len(park), len(park[0])
    for x in range(N):
        for y in range(M):
            if park[x][y] == "-1":
                for m in mats:
                    if x+m <= N and y+m <= M:
                        if is_empty(x, y, m) and ans < m:
                            ans = m
    return ans



print(solution([5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]])) # 3
# print(solution([5,3,2], [["A"]])) # -1
# print(solution([1], [["-1"]])) # -1