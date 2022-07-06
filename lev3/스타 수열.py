def solution(a):
    N = len(a)-1
    if not N: return 0

    # version1 - 1.600814453
    # idx = 0
    # cnt = dict()
    # while idx < N:
    #     if a[idx] not in cnt:
    #         cnt[a[idx]] = 0
    #     cnt[a[idx]] += 1
    #     if a[idx] == a[idx+1]:
    #         i = idx+2
    #         while i < N:
    #             if a[idx] != a[i]: break
    #             i += 1
    #         cnt[a[idx]] += 1
    #         idx = i
    #     else: idx += 1
    #
    # if a[-2] != a[-1]:
    #     if a[-1] not in cnt:
    #         cnt[a[-1]] = 0
    #     cnt[a[idx]] += 1

    # version2 - 1.4618284209999999
    # cnt = dict()
    # cnt[a[0]] = 1
    # for i in range(1, N):
    #     if a[i-1] == a[i] == a[i+1]: continue
    #     if a[i] not in cnt: cnt[a[i]] = 1
    #     else: cnt[a[i]] += 1
    #
    # if a[-2] != a[-1]:
    #     if a[-1] not in cnt:
    #         cnt[a[-1]] = 0
    #     cnt[a[-1]] += 1

    # k = sorted(cnt.items(), key=lambda x: x[1])[-1][0]
    # ans = 0
    # idx = 0
    # pre = -1
    # while idx < N:
    #     if a[idx] != k:
    #         if idx-1 > pre and a[idx-1] == k:
    #             ans += 2
    #         elif a[idx+1] == k:
    #             ans += 2
    #             idx += 1
    #         pre = idx
    #     idx += 1
    # return ans

    # code refactoring - 1.025373673
    dic = dict()
    for i, v in enumerate(a):
        if v not in dic: dic[v] = list()
        dic[v].append(i)

    N = len(a)-1
    ans = 0
    for k, v in dic.items():
        if len(v) <= ans // 2: continue
        now = a.copy()
        cnt = 0
        for j in v:
            if j > 0 and now[j-1] != k:
                now[j-1] = k
                cnt += 2
            elif j < N and now[j+1] != k:
                now[j+1] = k
                cnt += 2
        ans = ans if ans > cnt else cnt
    return ans


# print(solution([0])) # 0
# print(solution([0,1])) # 2
# print(solution([0,0,0,0])) # 0
# print(solution([1,2,3,3,5,3])) # 4
# print(solution([2,3,3,5,4,3])) # 6
# print(solution([0,3,3,0,7,2,0,2,2,0])) # 8
# print(solution([5,2,3,4,6,7,8,9,2,4,7,1,7,10])) # 6
# print(solution([5,2,2,4,2,3,4,1,4,6,4,7])) # 8
# print(solution([1,2,3,4,5,6,7,8,9,10])) # 2
print(solution([5,2,2,4,2,3,4,1,4,6,4,7,2,2,2,2])) # 8
print(solution([0,2,0,3,1,1,1,1,1,1,1,1,1,0,4])) # 6
print(solution([0,1,2,3,0])) # 4


if __name__ == "__main__":
    from timeit import Timer
    query = [[0], [0,1], [0,0,0,0], [1,2,3,3,5,3], [2,3,3,5,4,3], [0,3,3,0,7,2,0,2,2,0], [5,2,3,4,6,7,8,9,2,4,7,1,7,10],
             [5,2,2,4,2,3,4,1,4,6,4,7], [1,2,3,4,5,6,7,8,9,10], [5,2,2,4,2,3,4,1,4,6,4,7,2,2,2,2],
             [0,2,0,3,1,1,1,1,1,1,1,1,1,0,4], [0,2,0,3,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,4],
             [0,1,2,3,0], [0,1]*1000, [i for i in range(1000)]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))
