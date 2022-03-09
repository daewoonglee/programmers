import re


def solution(n, k):
    def baseb(n,k):
        q = n//k
        d = n%k
        if q == 0:
            return str(d)
        return baseb(q,k) + str(d)

    base_n = re.sub('0{2,}', '0', baseb(n, k))
    ans = 0
    for num in map(int, [b for b in base_n.split("0") if b]):
        if num == 1: continue
        if not [i for i in range(2, int(num**0.5)+1) if num % i == 0]:
           ans += 1
    return ans
    
        
print(solution(437674, 3))
print(solution(110011, 10))
print(solution(1000000,10))


