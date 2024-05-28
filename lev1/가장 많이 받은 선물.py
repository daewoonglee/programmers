def solution(friends, gifts):
    N = len(friends)
    friend_idx = {f: i for i, f in enumerate(friends)}
    gift_log = [[0]*N for _ in friends]
    for gift_row in gifts:
        friend1, friend2 = gift_row.split()
        gift_log[friend_idx[friend1]][friend_idx[friend2]] += 1
    print(f"gift_log: {gift_log}")

    gift_index = [sum(gift_log[j]) - sum([l[j] for l in gift_log]) for j in range(N)]
    print(f"gift index: {gift_index}")

    ans = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            gift_cnt1, gift_cnt2 = gift_log[i][j], gift_log[j][i]
            if gift_cnt1 == gift_cnt2:
                if gift_index[i] > gift_index[j]:
                    ans[i] += 1
                elif gift_index[i] < gift_index[j]:
                    ans[j] += 1
            else:
                ans[i if gift_cnt1 > gift_cnt2 else j] += 1
    print(f"ans: {ans}")
    return max(ans)


# print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])) # 2
# print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])) # 4
# print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])) # 0
print(solution(["a", "b", "c", "d", "e", "f"], ["a b"])) # 0
