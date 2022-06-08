import math
def solution(n, cores):
    N = len(cores)
    if n <= N: return n
    n -= N

    left, right = math.ceil(min(cores) * n / N), math.ceil(max(cores) * n / N)
    while left < right:
        mid = (right+left) // 2
        fin_cores = 0
        for c in cores:
            fin_cores += mid // c
        print(f"mid: {mid}, left: {left}, right: {right}, fin: {fin_cores}, n: {n}")
        if fin_cores >= n: right = mid
        else: left = mid+1
    print(f"out left: {left}, right: {right}, mid: {mid}")
    pre = sum([(right-1)//c for c in cores])
    cur = n-pre
    print(f"pre: {pre}, cur: {n - pre}")
    idx = 0
    for i, c in enumerate(cores):
        if right % c == 0: idx+=1
        if cur == idx: return i + 1
    return N


""" 
    1   2                       1   2   3
0   O   O   [1   2]             O   O   O   [1  2   3]
1   O       [3    ]             O           [4          ]
2   O   O   [4   5]             O   O       [5  6       ]
3   O       [6    ]             O       O   [7      8]

     1   2   3   1
0    O   O   O   O   [1  1   1   1]  0   1   2   3
1    O           O   [1  0   0   1]  4   5   6   7
2    O   O       O   [1  1   0   1]  8   9   10  11
3    O       O   O   [1  0   1   1]  12  13  14  15
4    O   O       O   [1  1   0   1]  16  17  18  19
5    O           O   [1  0   0   1]  20  21  22  23
6    O   O   O   O   [1  1   1   1]
7    O           O   [1  0   0   1] 
8    O   O       O   [1  1   0   1]  
9    O       O   O   [1  0   1   1]    
10   O   O       O   [1  1   0   1]  16  17  18  19
11   O           O   [1  0   0   1]  20  21  22  23
12   O   O   O   O   [1  1   1   1]
"""

# print(solution(6, [1, 2, 3])) # 2
# print(solution(22, [1, 2, 3, 1])) # 1
# print(solution(34, [1, 2, 3, 1])) # 4
print(solution(330, [1, 2, 3, 1])) # 1
# print(solution(324, [1, 2])) # 1
# print(solution(3, [1, 3])) # 1
