def solution(n):
    if n % 2 == 1: return 0
    alpha = 0
    for _ in range(n//2-1):
        alpha = alpha * 3 * 2 + 2
    print(f"alpha: {alpha}")
    return (3 ** (n//2) + alpha) % 1000000007

"""
n=홀수이면 0, 나올 수 있는 방법이 없음 (가로 길이 만족 할 수 없어서)
n   ans
2   3 + 0
4   9 + (0*3)*2 + 2 // 3 * 3 + (2)
6   27 + (2*3)*2 + 2  // 3 * 3 * 3 + (2) * 3 * 2 + (2)
8   81 + 70 + 2 // (2*3*3)*2*2 + 2
10  243 + (72*3)*2 + 2
"""

print(solution(2)) # 3
print(solution(4)) # 11
print(solution(6)) # 41
print(solution(8)) # 167 -> 153
