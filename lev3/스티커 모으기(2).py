def solution(sticker):
    N = len(sticker)
    if N <= 3: return max(sticker)

    if N % 2 == 0:
        even, odd = 0, 0
        for i, s in enumerate(sticker):
            if i % 2 == 0: even += s
            else: odd += s
        return even if even > odd else odd
    else:
        ans = 0
        for i in range(N):
            temp = sticker[i] + sum([sticker[(i+j*2)%N] for j in range(1, N//2)])
            ans = temp if ans < temp else ans
        return ans


# print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
# print(solution([1, 3, 2, 5, 4])) # 8
# print(solution([1])) # 1
# print(solution([1, 1, 1, 1, 1])) # 2
print(solution([14, 6, 5, 11, 3, 9, 2])) # 34
