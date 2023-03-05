def solution(n, m, section):
    # # 1.810782208
    # ans = 0
    # step = 0
    # for s in section:
    #     if step < s:
    #         step = m + s - 1
    #         ans += 1
    # return ans

    # code refactoring - 1.5863293029999999
    ans = 1
    step = section[0]
    for s in section:
        if s - step >= m:
            step = s
            ans += 1
    return ans


print(solution(8, 4, [2, 3, 6])) # 2
print(solution(5, 4, [1, 3])) # 1
print(solution(4, 1, [1, 2, 3, 4])) # 4
print(solution(20, 4, [1, 4, 5, 6, 7, 12, 14, 15])) # 3


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [8, 4, [2, 3, 6]],
        [5, 4, [1, 3]],
        [4, 1, [1, 2, 3, 4]],
        [20, 4, [1, 4, 5, 6, 7, 12, 14, 15]],
        [100000, 1, [i for i in range(1, 100001)]],
        [100000, 3, [i for i in range(1, 100001, 5)]],
        [100000, 10, [i for i in range(1, 100001)]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=100))
