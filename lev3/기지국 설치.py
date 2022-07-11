import math


def solution(n, stations, w):
    ans = 0
    step = w*2+1
    pre = 0
    for s in stations:
        ans += math.ceil((s-w-1-pre) / step)
        # print(f"s: {s}, s-w: {s-w}, pre: {pre}, ans: {ans}")
        pre = s+w
    # if pre < n: ans += math.ceil((n-pre) / step)

    print(f"pre: {pre}, ans: {ans}")
    if pre < n: ans += math.ceil((n-pre) / step)

    return ans


# print(solution(11, [4, 11], 1)) # 3
# print(solution(16, [9], 2))     # 3
# print(solution(11, [2,4,6,8,10], 1))    # 0
# print(solution(14, [2,4,6,8,10], 1))    # 1
# print(solution(15, [2,4,6,8,10], 1))    # 2
print(solution(10, [2,4,6,8,10], 2))    # 0
print(solution(12, [2,4,6,8,10], 2))    # 0
print(solution(13, [2,4,6,8,10], 2))    # 0
