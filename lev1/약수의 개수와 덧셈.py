def solution(left, right):
    ans = 0
    for n in range(left, right+1):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                cnt += 2 if n / i != i else 1
        ans += n if cnt % 2 == 0 else -n
    return ans


print(solution(13, 17))
print(solution(24, 27))
print(solution(1, 3))

