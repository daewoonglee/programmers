def solution(sticker):
    N = len(sticker)
    if N <= 1: return max(sticker)

    # if N % 2 == 0:
    #     even, odd = 0, 0
    #     for i, s in enumerate(sticker):
    #         if i % 2 == 0: even += s
    #         else: odd += s
    #     return even if even > odd else odd
    # else:
    dp1 = [0 for _ in sticker]
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    dp2 = [0 for _ in sticker]
    dp2[1] = sticker[1]
    for i in range(2, N-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    for i in range(2, N):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    s1, s2 = max(dp1), max(dp2)
    return s1 if s1 > s2 else s2


print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
# print(solution([1, 3, 2, 5, 4])) # 8
# print(solution([1])) # 1
# print(solution([1, 1, 1, 1, 1])) # 2

# print(solution([14, 6, 5, 11, 3, 9, 2])) # 34
# print(solution([14, 6, 5, 11, 3, 9, 2, 10, 11, 12, 13])) # 56
print(solution([4, 6, 50, 11, 30, 9, 20, 10, 11, 12, 13])) # 56
