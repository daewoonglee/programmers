def solution(n, s):
    # 1.577689774
    if n > s: return [-1]
    # ans = []
    # for i in range(n, 0, -1):
    #     ans.append(s//i)
    #     s -= ans[-1]
    # return ans

    # code refactoring - 0.072525688, 몫에서 나머지 값의 범위만큼 맨 뒤에서부터 +1 해주면 됨
    d = s % n
    ans = [s//n]*n
    for i in range(1, d+1):
        ans[-i] += 1
    return ans


# print(solution(2, 9))
print(solution(2, 1))
# print(solution(3, 12))
print(solution(3, 11))
# print(solution(3, 9))


if __name__ == "__main__":
    from timeit import Timer
    query = [[2,9],
             [2,1],
             [3,12],
             [3,11],
             [3,9],
             [1000,10000]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
