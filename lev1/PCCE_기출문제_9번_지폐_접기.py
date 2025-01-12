def solution(wallet, bill):
    ans = 0
    wallet.sort()
    bill.sort()
    while not (bill[0] <= wallet[0] and bill[1] <= wallet[1]):
        bill[1] //= 2
        bill.sort()
        ans += 1
    return ans


print(solution([30, 15], [26, 17])) # 1
print(solution([50, 50], [100, 241])) # 4
print(solution([10, 10], [10, 10])) # 0
