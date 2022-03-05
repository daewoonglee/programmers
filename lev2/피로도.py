from itertools import permutations


def solution(k, dungeons):
    # 0.2505955380038358
    #ans = 0
    #for p_dungeons in permutations(dungeons, len(dungeons)):
    #    cnt = 0
    #    N = k
    #    for d in p_dungeons:
    #        if N >= d[0]:
    #            cnt += 1
    #            N -= d[1]
    #    if ans < cnt:
    #        ans = cnt
    #return ans

    # code refactoring - 0.19738401799986605
    ans = 0
    for p_dungeons in permutations(dungeons):
        N, cnt = k, 0
        for need, cost in p_dungeons:
            if N >= need:
                N -= cost
                cnt += 1
        if ans < cnt:
            ans = cnt
    return ans


print(solution(80, [[80,20], [50,40], [30,10]]))
print(solution(100, [[10,10], [20,20], [30,30], [40,10]]))
print(solution(16, [[4,1],[8,2],[12,3],[16,4]]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[80, [[80,20], [50,40], [30,10]]], [100, [[10,10], [20,20], [30,30], [40,10]]], [16, [[4,1],[8,2],[12,3],[16,4]]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

