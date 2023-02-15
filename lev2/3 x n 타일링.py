def solution(n):
    if n % 2 == 1: return 0
    n //= 2
    if n <= 1: return [0, 3][n]

    tile = [3]
    for i in range(1, n):
        tile.append(sum([t*3 if j == 0 else t * 2 for j, t in enumerate(tile[::-1])])+2)
    return tile[n-1] % 1000000007

"""
n   ans
0   0 =  0
2   3 =  3
4   11 = 3*3 + 2                = f(2)*3 + 2
6   41 = 11*3 + 3*2 + 2         = f(4)*3 + f(2)*2 + 2
8  153 = 41*3 + 11*2 + 3*2 + 2  = f(6)*3 + f(4)*2 + f(2)*2 + 2

f(N) = f(N-2)*3 + f(N-4)*2 + f(N-6)*2 + ... + f(2)*2 + 2
"""

# print(solution(0)) # 0
# print(solution(1)) # 0
# print(solution(2)) # 3
# print(solution(4)) # 11
# print(solution(6)) # 41
print(solution(8)) # 153
