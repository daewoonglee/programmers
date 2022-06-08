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
        if fin_cores >= n: right = mid
        else: left = mid+1

    # 0.229796191
    # pre = sum([(right-1)//c for c in cores])
    # cur = n-pre
    # idx = 0
    # for i, c in enumerate(cores):
    #     if right % c == 0: idx+=1
    #     if cur == idx: return i + 1

    # code refactoring - 0.208195125
    for c in cores:
        n -= (right-1)//c
    for i, c in enumerate(cores):
        if right % c == 0:
            n -= 1
            if n == 0:
                return i+1

    return N


# print(solution(6, [1, 2, 3])) # 2
# print(solution(22, [1, 2, 3, 1])) # 1
# print(solution(34, [1, 2, 3, 1])) # 4
print(solution(330, [1, 2, 3, 1])) # 1
# print(solution(324, [1, 2])) # 1
# print(solution(3, [1, 3])) # 1


if __name__ == "__main__":
    from timeit import Timer
    query = [[6, [1, 2, 3]],
             [22, [1, 2, 3, 1]],
             [34, [1, 2, 3, 1]],
             [330, [1, 2, 3, 1]],
             [324, [1, 2]],
             [3, [1, 3]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
