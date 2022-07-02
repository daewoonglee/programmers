def solution(a):
    N = len(a)
    if N < 3: return N

    min_l = [a[0]] * (N-2)
    for i in range(2, N-1): # 1번 인덱스의 left는 0번 인덱스가 확정이기 때문에 2번 인덱스부터 left 판별
        min_l[i-1] = a[i-1] if a[i-1] < min_l[i-2] else min_l[i-2]

    min_r = [a[-1]] * (N-2)
    for i in range(N-3, 0, -1): # N-2번 인덱스의 right은 N-1번 인덱스 확정이기 때문에 N-3번 인덱스부터 right 판별
        min_r[i-1] = min_r[i] if min_r[i] < a[i+1] else a[i+1]

    ans = 2
    for i, n in enumerate(a[1:-1]):
        if min_l[i] > n or min_r[i] > n: ans += 1
    return ans


# print(solution([9,-1,-5])) # 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # 6
# print(solution([-16,27,-65,-33,-61,-64])) # 3
