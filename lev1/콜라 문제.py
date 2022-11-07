def solution(a, b, n):
    # 0.067494172
    # ans = 0
    # while a <= n:
    #     q, d = n//a*b, n % a
    #     n = q + d
    #     ans += q
    # return ans

    # code refactoring - 0.014339743000000002
    return (n-b) // (a-b)*b


print(solution(2, 1, 20)) # 19
print(solution(3, 1, 20)) # 9
print(solution(2, 1, 23)) # 22


if __name__ == "__main__":
    from timeit import Timer
    query = [[2, 1, 20],
             [3, 1, 20],
             [2, 1, 23],
             [10, 7, 100000]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
