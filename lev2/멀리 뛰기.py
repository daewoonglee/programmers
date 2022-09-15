def solution(n):
    ans = [1, 1]
    idx = 0
    for i in range(n-1):
        idx = i%2
        ans[idx] += ans[idx-1]
    return ans[idx] % 1234567


print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
