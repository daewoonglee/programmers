def solution(n):
    # 1.920356184
    # ans = [1, 1]
    # idx = 0
    # for i in range(n-1):
    #     idx = i%2
    #     ans[idx] += ans[idx-1]
    # return ans[idx] % 1234567

    # code refactoring - 0.82522538
    if n == 1: return 1
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a+b
    return b % 1234567


print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))


if __name__ == "__main__":
    from timeit import Timer
    query = [4, 5, 6, 7, 100, 1000]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
