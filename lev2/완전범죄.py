import sys
sys.setrecursionlimit(10000)


def solution(info, n, m):
    def steal(a, b, depth):
        nonlocal ans
        if depth == N:
            ans = a if a < ans else ans
        else:
            steal_a = a+info[depth][0]
            steal_b = b+info[depth][1]

            if steal_a < n:
                steal(steal_a, b, depth+1)
            if steal_b < m:
                steal(a, steal_b, depth+1)

    N = len(info)
    ans = float('inf')
    steal(0, 0, 0)
    return ans if ans != float('inf') else -1



print(solution([[1, 2], [2, 3], [2, 1]], 4, 4)) # 2
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7)) # 0
print(solution([[3, 3], [3, 3]], 7, 1)) # 6
print(solution([[3, 3], [3, 3]], 6, 1)) # -1
print(solution([[2, 2], [1, 3], [2, 3], [3, 1]], 7, 9)) # 1
print(solution([[2, 2], [1, 3], [2, 3], [3, 1]], 7, 7)) # 1
print(solution([[1, 2], [2, 3], [3, 1]], 6, 1)) # -1
