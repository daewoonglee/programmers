def solution(n, s):
    if n > s: return [-1]
    ans = []
    for i in range(n, 0, -1):
        ans.append(s//i)
        s -= ans[-1]
    return ans

# n=3, s=12, [4,4,4]
# n=3, s=11, [3,4,4]
"""
n = 11
1 1 9
1 2 8
1 3 7
1 4 6
1 5 5

2 2 7 28
2 3 6 36
2 4 5 40

3 3 5 45
3 4 4 48
"""

# n=3, s=9, [3,3,3]

# print(solution(2, 9))
# print(solution(2, 1))
# print(solution(3, 12))
print(solution(3, 11))
# print(solution(3, 9))
