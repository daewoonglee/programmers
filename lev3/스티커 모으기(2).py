def solution(sticker):
    N = len(sticker)
    if N <= 1: return max(sticker)

    # 0.913502072
    if N % 2 == 0:
        even, odd = 0, 0
        for i, s in enumerate(sticker):
            if i % 2 == 0: even += s
            else: odd += s
        return even if even > odd else odd
    else:
        # 1.459002315
        dp1 = [0] * N
        dp1[0] = sticker[0]
        dp1[1] = sticker[0]

        dp2 = [0] * N
        dp2[1] = sticker[1]

        for i in range(2, N-1): dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
        for i in range(2, N): dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
        return dp1[-2] if dp1[-2] > dp2[-1] else dp2[-1]


print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
# print(solution([1, 3, 2, 5, 4])) # 8
# print(solution([1])) # 1
# print(solution([1, 1, 1, 1, 1])) # 2
# print(solution([14, 6, 5, 11, 3, 9, 2])) # 34
# print(solution([14, 6, 5, 11, 3, 9, 2, 10, 11, 12, 13])) # 56
print(solution([4, 6, 50, 11, 30, 9, 20, 10, 11, 12, 13])) # 124


if __name__ == "__main__":
    from timeit import Timer
    query = [[14, 6, 5, 11, 3, 9, 2, 10],
             [1, 3, 2, 5, 4],
             [1],
             [1, 1, 1, 1, 1],
             [14, 6, 5, 11, 3, 9, 2],
             [14, 6, 5, 11, 3, 9, 2, 10, 11, 12, 13],
             [4, 6, 50, 11, 30, 9, 20, 10, 11, 12, 13],
             [i for i in range(1,100)],
             [i for i in range(1,99)]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
