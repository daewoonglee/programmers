def solution(a, b, n):
    ans = 0
    while a <= n:
        q, d = n//a*b, n % a
        n = q + d
        ans += q
    return ans


print(solution(2, 1, 20)) # 19
print(solution(3, 1, 20)) # 9
print(solution(2, 1, 23)) # 22
