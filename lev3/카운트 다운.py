def solution(target):
    def countdown(n, q):
        if n == 0: return [q, 0] if x != 50 else [q, q]
        elif n > 20 and n % 3 == 0 or (n <= 40 and n % 2 == 0): return [q+1, 0] if x != 50 else [q+1, q]
        elif n == 50: return [q+1, 1]
        elif n > 50: return [q+2, 2]
        elif n < 20: return [q+1, 1]
        elif n < 40: return [q+2, 2]
        else: return [q+2, 1]

    ans = [[] for _ in range(5)]
    for i, x in enumerate([60, 57, 54, 51, 50]): # 20(60), 19(57), 18(54), 17(51), 50(bull)
        xq, xd = divmod(target, x)
        ans[i] = countdown(xd, xq)

    return min(ans, key=lambda x: (x[0], -x[1]))


print(solution(21)) # [1,0]
print(solution(58)) # [2,2]
print(solution(100000)) # [1667, 0]
# print(solution(1)) # [1,1]
# print(solution(35)) #[2,2]
# print(solution(49)) #[2,1]
# print(solution(40)) #[1,0]
# print(solution(41)) #[2,1]
# print(solution(47)) #[2,1]
# print(solution(180)) #[3,0]
# print(solution(250)) #[5,5]
# print(solution(50)) # [1,1]
# print(solution(37)) # [2,2]
