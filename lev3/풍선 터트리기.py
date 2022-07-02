def solution(a):
    # 1.074001974
    # N = len(a)
    # if N < 3: return N
    #
    # min_l = [a[0]] * (N-2)
    # for i in range(2, N-1): # 1번 인덱스의 left는 0번 인덱스가 확정이기 때문에 2번 인덱스부터 left 판별
    #     min_l[i-1] = a[i-1] if a[i-1] < min_l[i-2] else min_l[i-2]
    #
    # min_r = [a[-1]] * (N-2)
    # for i in range(N-3, 0, -1): # N-2번 인덱스의 right은 N-1번 인덱스 확정이기 때문에 N-3번 인덱스부터 right 판별
    #     min_r[i-1] = min_r[i] if min_r[i] < a[i+1] else a[i+1]
    #
    # ans = 2
    # for i, n in enumerate(a[1:-1]):
    #     if min_l[i] > n or min_r[i] > n: ans += 1
    # return ans

    # code refactoring - 0.364075461
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        i = 1
        while m != M:
            if m >= a[i]:
                m = a[i]
                answer += 1
            i += 1
        a.reverse()
    return answer


# print(solution([9,-1,-5])) # 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # 6
# print(solution([-16,27,-65,-33,-61,-64])) # 3


if __name__ == "__main__":
    from timeit import Timer
    query = [[9,-1,-5],
             [-16,27,65,-2,58,-92,-71,-68,-61,-33],
             [-16,27,-65,-33,-61,-64],
             [i for i in range(-100, 100)]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
