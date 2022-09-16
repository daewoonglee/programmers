import math
from itertools import permutations


def solution(n, k):
    li = [i for i in range(1, n+1)]
    ans = []
    while n:
        f = math.factorial(n)
        g = f // n
        q, d = (k-1) // g, k % g
        print(f"before n: {n}, f: {f}, k: {k}, g: {g}, q: {q}, d: {d}")
        ans.append(li.pop(q))
        n -= 1
        k = d

    return ans


    # return [q] + list(list(permutations([i for i in range(1, n+1) if i != q], n-1))[d])

print(solution(3, 1))
print(solution(3, 2))
print(solution(3, 3))
print(solution(3, 4))
print(solution(3, 5))
print(solution(4, 5))
print(solution(4, 10))
