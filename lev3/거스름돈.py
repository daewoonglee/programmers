def solution(n, money):
    def get_change(change, idx):
        if idx >= len(money) or money[idx] > change: return
        q = change // money[idx]
        for sub_q in range(q+1):
            diff = change-sub_q*money[idx]
            if diff == 0: ans[0] += 1
            else: get_change(diff, idx+1)

    ans = [0]
    money.sort()
    get_change(n, 0)

    return ans[0] % 1000000007


"""
n=5, money=[1,2,3,4]
1 1 1 1 1
1 1 1 2
1 1 3
1 2 2
1 4
2 3

n=9, money=[1,2,3,4]
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 2
1 1 1 1 1 1 3
1 1 1 1 1 2 2
1 1 1 1 1 4
1 1 1 1 2 3
1 1 1 2 2 2
1 1 1 2 4
1 1 1 3 3
1 1 2 2 3
1 1 4 3
1 2 2 2 2
1 2 2 4
1 2 3 3
1 4 4
2 2 2 3
2 4 3
3 3 3
"""

# print(solution(5, [1,2,5])) # 4
# print(solution(5, [1,2,3,4])) # 6
# print(solution(6, [1,2,3]))   # 7
print(solution(9, [1,2,3,4])) # 18
