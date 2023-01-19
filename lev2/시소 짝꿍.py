def solution(weights):
    def is_same(n1, n2):
        for s1 in seesaw:
            for s2 in seesaw:
                if n1 / s1 == n2 / s2:
                    return 1
        return 0

    N = len(weights)
    ans = 0
    seesaw = [2, 3, 4]
    for i, k in enumerate(weights):
        for j in range(i+1, N):
            ans += is_same(k, weights[j])
    return ans


print(solution([100,180,360,100,270])) # 4
print(solution([100,100])) # 1
print(solution([100,100,100])) # 3
print(solution([100,100,100,100])) # 6
