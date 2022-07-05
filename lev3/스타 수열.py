def solution(a):
    N = len(a)-1
    if not N: return 0

    idx = 0
    cnt = dict()
    # index_list = dict()
    while idx < N:
        if a[idx] not in cnt:
            cnt[a[idx]] = 0
            # index_list[a[idx]] = []

        # index_list[a[idx]].append(idx)
        cnt[a[idx]] += 1
        if a[idx] == a[idx+1]:
            i = idx+2
            while i < N:
                if a[idx] != a[i]: break
                i += 1
            # index_list[a[idx]].append(i-1)
            cnt[a[idx]] += 1
            idx = i
        else: idx += 1

    if a[-2] != a[-1]:
        if a[-1] not in cnt:
            cnt[a[-1]] = 0
            # index_list[a[-1]] = []
        # index_list[a[-1]].append(N)
        cnt[a[idx]] += 1

    print(f"cnt: {cnt}")
    # print(f"idx: {index_list}")

    k = sorted(cnt.items(), key=lambda x: x[1])[-1][0]
    ans = 0
    # check_list = []
    # for idx in index_list[k]:
    #     if idx > 0 and a[idx] != a[idx-1] and idx-1 not in check_list:
    #         check_list.append(idx-1)
    #         ans += 2
    #     elif idx < N-1 and a[idx] != a[idx+1] and idx+1 not in check_list:
    #         check_list.append(idx+1)
    #         ans += 2

    idx = 0
    pre = -1
    while idx < N:
        # print(f"before: {idx}, pre: {pre}, idx: {idx}")
        if a[idx] != k:
            if idx-1 > pre and a[idx-1] == k:
                # pre = idx
                ans += 2
                # print(f"+1: {idx}, ans: {ans}")
            elif a[idx+1] == k:
                ans += 2
                idx += 1
                # pre = idx
                # print(f"+2: {idx}, ans: {ans}")
            pre = idx
        idx += 1
        # print(f"after: {idx}, pre: {pre}, idx: {idx}\n")
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
# print(solution([5,2,2,4,2,3,4,1,4,6,4,7,2,2,2,2])) # 8
# print(solution([0,2,0,3,1,1,1,1,1,1,1,1,1,0,4])) # 6
print(solution([0,1,2,3,0])) # 4
print(solution([0,1]*1000)) # 4
