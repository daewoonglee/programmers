def solution(n):
    # if n % 2 == 1: return 0
    # n //= 2
    # if n <= 1: return [0, 3][n]
    #
    # tile = [3]
    # for i in range(1, n):
    #     # 10.483321146
    #     # tile.append(sum([t*3 if j == 0 else t * 2 for j, t in enumerate(tile[::-1])])+2)
    #
    #     # code refactoring 01 - 2.616065683
    #     # tile.append(tile[i-1]*3 + sum(tile[:i-1])*2 +2)
    # # return tile[n - 1] % 1000000007
    #
    #     # code refactoring 02 - 0.30438955700000003
    #     tile.append((tile[i-1]*3 + sum(tile[:i-1])*2 + 2) % 1000000007)
    # return tile[n-1]

    # code refactoring 03 - 0.005943779999999999
    # f(N-2)*4 - f(N-4)
    if n % 2 == 1: return 0
    pre = cur = 1
    for _ in range(n // 2):
        pre, cur = cur, (4 * cur - pre) % 1000000007
    return cur


# print(solution(0)) # 0
# print(solution(1)) # 0
# print(solution(2)) # 3
# print(solution(4)) # 11
# print(solution(6)) # 41
print(solution(8)) # 153


if __name__ == "__main__":
    from timeit import Timer
    query = [
        0, 1, 2, 4, 6, 8, 1000, 2000, 5000
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10))
