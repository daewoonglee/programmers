def solution(left, right):
    # 1.5910107344388962
    #ans = 0
    #for n in range(left, right+1):
    #    cnt = 0
    #    for i in range(1, int(n**0.5)+1):
    #        if n % i == 0:
    #            cnt += 2 if n / i != i else 1
    #    ans += n if cnt % 2 == 0 else -n
    #return ans

    # code refactoring (R) - 0.20098081603646278
    return sum([-n if (n**0.5).is_integer() else n for n in range(left, right+1)])


print(solution(13, 17))
print(solution(24, 27))
print(solution(1, 3))


if __name__ == "__main__":
    from timeit import Timer
    query = [[13,17], [24,27], [1,3], [1,1000]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))

