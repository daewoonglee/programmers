def solution(n, money):
    # 0.219994836
    # money.sort()
    # ans = [1 if i % money[0] == 0 else 0 for i in range(n+1)]
    # N = len(ans)-1
    # for m in money[1:]:
    #     for i in range(N):
    #         if i+1 < m: continue
    #         ans[i+1] += ans[i-m+1]
    # return ans[-1] % 1000000007

    # code refactoring - 0.16052092099999998
    arr = [1] + [0]*n
    for c in money:
        for i in range(c, n+1):
            arr[i] += arr[i-c]
    return arr[-1] % 1000000007


print(solution(5, [1,2,5])) # 4
print(solution(5, [1,2,3,4])) # 6
print(solution(5, [2,5])) # 1
# print(solution(6, [1,2,3]))   # 7
# print(solution(9, [1,2,3,4])) # 18


if __name__ == "__main__":
    from timeit import Timer
    query = [[5, [1,2,5]],
             [5, [1,2,3,4]],
             [5, [2,5]],
             [6, [1,2,3]],
             [9, [1,2,3,4]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
