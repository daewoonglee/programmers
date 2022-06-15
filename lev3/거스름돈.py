def solution(n, money):
    def get_change(idx, change):
        for j in range(idx, N):
            mul = 1
            while 1:
                d = change-money[j]*mul
                if d > 0: mul += 1
                else:
                    if d == 0:
                        # print(f"while sub money: {money[j]}, idx: {j}, mul: {mul}, diff: {d}")
                        ans[0] += 1
                    for sub_mul in range(mul-1, 0, -1):
                        get_change(j+1, change-money[j]*sub_mul)
                    break

    ans = [0]
    money.sort()
    N = len(money)
    for i, m in enumerate(money):
        q = n // m
        for sub_q in range(q, 0, -1):
            diff = n-sub_q*m
            # if m == 1 and sub_q == 4:
            #     get_change(i+1, diff)
            if diff == 0:
                # print(f"m: {m}, n: {n}, sq: {sub_q}, diff: {diff}")
                ans[0] += 1
            else:
                # print(f"stand money: {m}, sub q: {sub_q}, n: {n}")
                get_change(i+1, diff)
                # print()
    return ans[0] % 1000000007



"""
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

# print(solution(5, [1,2,5]))
# print(solution(5, [1,2,3,4]))
# print(solution(6, [1,2,3]))
print(solution(9, [1,2,3,4])) # 18
