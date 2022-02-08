from itertools import combinations
def solution(nums):
    # 1.3407424110919237
    #ans = 0
    #for c in combinations(nums, 3):
    #    total = sum(c)
    #    flag = False
    #    for n in range(2, int(total**0.5)+1):
    #        if total % n == 0:
    #            flag = True
    #            break
    #    if not flag:
    #        ans += 1
    #return ans

    # code refactoring - 1.3150121178478003
    ans = 0
    for c in combinations(nums, 3):
        total = sum(c)
        for n in range(2, int(total**0.5)+1):
            if total % n == 0:
                break
        else:
            ans += 1
    return ans


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
print(solution([i for i in range(1, 51)]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[1,2,3,4], [1,2,7,6,4], [i for i in range(1,51)]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=100))

