def solution(friends, gifts):
    N = len(friends)
    friend_idx = {f: i for i, f in enumerate(friends)}
    log = [[0]*N for _ in friends]
    for gift_row in gifts:
        friend1, friend2 = gift_row.split()
        log[friend_idx[friend1]][friend_idx[friend2]] += 1
    print(f"log: {log}")

    gift_index = [0] * N
    for j in range(N):
        give = sum(log[j])
        take = sum([l[j] for l in log])
        gift_index[j] = give-take
    print(f"gift index: {gift_index}")

    ans = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            friend1, friend2 = log[i][j], log[j][i]
            if friend1 == friend2:
                if gift_index[i] > gift_index[j]:
                    ans[i] += 1
                elif gift_index[i] < gift_index[j]:
                    ans[j] += 1
            elif friend1 > friend2:
                ans[i] += 1
            else:
                ans[j] += 1
    print(f"ans: {ans}")
    return max(ans)


# print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])) # 2
# print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])) # 4
# print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])) # 0
print(solution(["a", "b", "c", "d", "e", "f"], ["a b"])) # 0
