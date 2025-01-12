def solution(wallet, bill):
    ans = 0
    while not ((bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[0] <= wallet[1] and bill[1] <= wallet[0])):
        bill[1 if bill[0] < bill[1] else 0] //= 2
        ans += 1
    return ans


print(solution([30, 15], [26, 17])) # 1
print(solution([50, 50], [100, 241])) # 4
print(solution([10, 10], [10, 10])) # 0
