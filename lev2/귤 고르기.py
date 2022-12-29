from collections import Counter


def solution(k, tangerine):
    ans = 0
    values = sorted(Counter(tangerine).values(), key=lambda x: x, reverse=True)
    for v in values:
        if k > 0:
            ans += 1
            k -= v
        else: break
    return ans


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1
