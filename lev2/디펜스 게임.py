import heapq


def solution(n, k, enemy):
    invincibility = enemy[:k]
    heapq.heapify(invincibility)
    ans = k
    for e in enemy[k:]:
        if e > invincibility[0]:
            n -= invincibility[0]
            heapq.heappop(invincibility)
            heapq.heappush(invincibility, e)
        else:
            n -= e

        if n < 0:
            break
        ans += 1
    return ans if k < len(enemy) else len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(7, 3, [4, 2, 1, 3, 1, 4, 5, 3])) # 7
print(solution(7, 3, [4, 4, 4, 5, 2, 1, 1])) # 6
print(solution(7, 3, [2, 4, 3, 3, 5, 4, 3])) # 5
print(solution(7, 3, [4, 2, 3, 2, 5, 3, 6])) # 6
print(solution(2, 4, [3, 3, 3, 3])) # 4
print(solution(13, 5, [3, 3, 3, 3])) # 4
