def solution(k, score):
    N = k if k < len(score) else len(score)
    ans = [score[0]]
    for s in score[1:N]:
        if s < ans[-1]: ans.append(s)
        else: ans.append(ans[-1])
    rank = sorted(score[:N], reverse=True)
    # print(ans)
    for s in score[N:]:
        if rank[-1] < s:
            rank[-1] = s
            rank.sort(reverse=True)
        ans.append(rank[-1])
    return ans


print(solution(3, [10, 100, 20, 150, 1, 100, 200])) # [10, 10, 10, 20, 20, 100, 100]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])) # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
print(solution(100, [0, 1000, 0, 0, 0, 0, 110, 0, 10, 1])) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(solution(3, [0, 1000, 0, 0, 0, 0, 110, 0, 10, 1])) # [0, 0, 0, 0, 0, 0, 0, 0, 10, 10]
print(solution(100, [100, 1000, 10, 1, 0, 0, 110, 0, 10, 1])) # [100, 100, 10, 1, 0, 0, 0, 0, 0, 0]
