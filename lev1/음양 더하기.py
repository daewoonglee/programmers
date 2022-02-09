def solution(absolutes, signs):
    # 0.07790890894830227
    #ans = 0
    #for a, s in zip(absolutes, signs):
    #    ans += a if s else -a
    #return ans

    # 0.08520650677382946 (callback function)
    return sum([a if s else -a for a, s in zip(absolutes, signs)])


print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[[4,7,12],[True, False, True]], [[1,2,3],[False,False,True]], [[i for i in range(1, 100)], [False if i % 2 == 0 else True for i in range(99)]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

