def solution(n, money):
    money.sort()
    ans = [1 if i % money[0] == 0 else 0 for i in range(n+1)]
    N = len(ans)-1
    for m in money[1:]:
        for i in range(N):
            if i+1 < m: continue
            ans[i+1] += ans[i-m+1]
    return ans[-1] % 1000000007


"""
            0           1       2           3       4           5
1           1 (0,0)   1 (0,1)   1 (0,2)   1 (0,3)   1 (0,4)   1 (0,5)
1,2         1 (1,0)   1 (1,1)   2 (1,2)   2 (1,3)   3 (1,4)   3 (1,5) 
1,2,3       1 (2,0)   1 (2,1)   2 (2,2)   3 (2,3)   4 (2,4)   5 (2,5)
1,2,3,4     1 (3,0)   1 (3,1)   2 (3,2)   3 (3,3)   5 (3,4)   6 (3,5)

            0   1   2   3   4   5
1           1   1   1   1   1   1
1,2         1   1   2   2   3   3 
1,2,5       1   1   2   2   3   4

            0   1   2   3   4   5
2           1   0   1   0   1   0
2,5         1   0   1   0   1   1
"""

print(solution(5, [1,2,5])) # 4
print(solution(5, [1,2,3,4])) # 6
print(solution(5, [2,5])) # 1
# print(solution(6, [1,2,3]))   # 7
# print(solution(9, [1,2,3,4])) # 18
