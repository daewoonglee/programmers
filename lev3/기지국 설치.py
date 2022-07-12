import math


def solution(n, stations, w):
    # 0.141598809
    # ans = 0
    # step = w*2+1
    # pre = 0
    # for s in stations:
    #     ans += math.ceil((s-w-1-pre) / step)
    #     pre = s+w
    # return ans + math.ceil((n-pre)/step) if pre < n else ans

    # code refactoring - 0.09231730899999999
    bef =- w
    cnt = 0
    step = w*2+1
    for s in stations:
        cnt += (s-bef-1)//step
        bef = s
        print(f"cnt: {cnt}, bef: {bef}")
    return cnt + (n+w-bef)//step


# print(solution(11, [4, 11], 1)) # 3
print(solution(16, [9], 2))     # 3
# print(solution(11, [2,4,6,8,10], 1))    # 0
# print(solution(14, [2,4,6,8,10], 1))    # 1
# print(solution(15, [2,4,6,8,10], 1))    # 2
# print(solution(10, [2,4,6,8,10], 2))    # 0
# print(solution(12, [2,4,6,8,10], 2))    # 0
# print(solution(13, [2,4,6,8,10], 2))    # 1


if __name__ == "__main__":
    from timeit import Timer
    query = [[11, [4,11], 1],
             [16, [9], 2],
             [11, [2,4,6,8,10], 1],
             [14, [2,4,6,8,10], 1],
             [15, [2,4,6,8,10], 1],
             [10, [2,4,6,8,10], 2],
             [12, [2,4,6,8,10], 2],
             [13, [2,4,6,8,10], 2],
             [10000000, [100, 1000, 10000], 2]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
