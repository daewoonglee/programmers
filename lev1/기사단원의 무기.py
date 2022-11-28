def solution(number, limit, power):
    ans = 1
    for n in range(2, number+1):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if n // i != i and n % (n // i) == 0: cnt +=1
                cnt += 1
        ans += cnt if cnt <= limit else power
    return ans


print(solution(5, 3, 2)) # 10
print(solution(10, 3, 2)) # 21
