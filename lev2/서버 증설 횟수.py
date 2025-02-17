def solution(players, m, k):
    N = len(players)
    servers = [0] * N
    ans = 0
    for i, player in enumerate(players):
        if player > servers[i] * m:
            server_num = (player-(servers[i]*m)) // m
            for j in range(i, i+k):
                if j >= N: break
                servers[j] += server_num
            ans += server_num
    return ans



# print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5)) #7
print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1)) #11
# print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1)) # 12