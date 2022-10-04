def solution(begin, end):
    MAX = 10000000
    ans = []
    if begin == 1:
        ans.append(0)
        begin += 1

    for num in range(begin, end+1):
        for n in range(2, int(num**0.5)+1):
            if num % n == 0 and num // n <= MAX:
                ans.append(num//n)
                break
        else: ans.append(1)
    return ans


print(solution(1, 10))
print(solution(1000000000-1, 1000000000))
