def solution(target):
    def countdown(n, q, m):
        print(f"n: {n}, q: {q}, m: {m}")
        if n == 0: return [q, m]
        elif n > 20 and (n % 3 == 0 or (n <= 40 and n % 2 == 0)): return [q+1, m]
        elif n == 50 or n <= 20: return [q+1, m+1]
        elif n > 50 or n < 40: return [q+2, m+2]
        else: return [q+2, m+1]

    ans = [[] for _ in range(5)]
    for i, x in enumerate([60, 57, 54, 51, 50]): # 20(60), 19(57), 18(54), 17(51), 50(bull)
        xq, xd = divmod(target, x)
        ans[i] = countdown(xd, xq, xq if x == 50 else 0)
    print(ans)

    return min(ans, key=lambda x: (x[0], -x[1]))


# print(solution(21)) # [1,0]
# print(solution(58)) # [2,2]
# print(solution(100000)) # [1667, 0]
# print(solution(1)) # [1,1]
# print(solution(35)) #[2,2]
# print(solution(49)) #[2,1]
# print(solution(40)) #[1,0]
# print(solution(41)) #[2,1]
# print(solution(47)) #[2,1]
# print(solution(180)) #[3,0]
# print(solution(250)) #[5,5]
# print(solution(103)) # [3,3]
# print(solution(102)) # [2,0]
# print(solution(101)) # [2,1]
print(solution(173)) # [4,3]
# print(solution(191)) # [2,1]
# print(solution(197)) # [2,1]
# 141, 147 -> 3, 1
# 191, 197 -> 4, 2
# 241, 247 -> 5, 3
# print(solution(37)) # [2,2]
