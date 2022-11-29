def solution(number, limit, power):
    # # 3.3446166020000003
    # ans = 1
    # for n in range(2, number+1):
    #     cnt = 2
    #     for i in range(2, int(n**0.5)+1):
    #         if n % i == 0:
    #             if n // i == i: cnt += 1
    #             else: cnt += 2
    #     ans += cnt if cnt <= limit else power
    # return ans

    # code refactoring - 1.0395714249999999
    ans = 0
    div = [0] * (number + 1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            div[j] += 1
    for d in div:
        ans += d if d <= limit else power
    return ans


print(solution(5, 3, 2)) # 10
print(solution(10, 3, 2)) # 21


if __name__ == "__main__":
    from timeit import Timer
    query = [[5, 3, 2],
             [10, 3, 2],
             [100, 50, 50],
             [1000, 50, 50],
             [10000, 50, 50]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=100))
