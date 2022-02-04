def solution(n):
    for i in range(2, n):
        if n % i == 1: return i
    return n


print(solution(10))
print(solution(12))
print(solution(1001))
print(solution(100001)) 

