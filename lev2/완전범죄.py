def solution(info, n, m):
    def steal(a, b, depth):
        nonlocal ans
        k = f"{depth}_{a}_{b}"
        if depth == N:
            ans = a if a < ans else ans
        elif k not in memo:
            memo.append(k)
            steal_a = a+info[depth][0]
            steal_b = b+info[depth][1]

            if steal_a < n and steal_a < ans:
                steal(steal_a, b, depth+1)
            if steal_b < m and a < ans:
                steal(a, steal_b, depth+1)

    N = len(info)
    ans = float('inf')
    memo = list()
    steal(0, 0, 0)
    return ans if ans != float('inf') else -1


print(solution([[1, 2], [2, 3], [2, 1]], 4, 4)) # 2
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7)) # 0
print(solution([[3, 3], [3, 3]], 7, 1)) # 6
print(solution([[3, 3], [3, 3]], 6, 1)) # -1
print(solution([[2, 2], [1, 3], [2, 3], [3, 1]], 7, 9)) # 1
print(solution([[2, 2], [1, 3], [2, 3], [3, 1]], 7, 7)) # 1
print(solution([[1, 2], [2, 3], [3, 1]], 6, 1)) # -1
