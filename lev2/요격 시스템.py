def solution(targets):
    # # 1.652443539
    # ans = 0
    # targets.sort()
    # while targets:
    #     s, e = targets.pop()
    #     while targets and targets[-1][0] <= s < targets[-1][1]:
    #         targets.pop()
    #     ans += 1
    # return ans

    # # code refactoring - 1.336575733
    # ans = 1
    # targets.sort()
    # s, e = targets[-1]
    # for i in range(len(targets)-2, -1, -1):
    #     x1, x2 = targets[i]
    #     if not x1 <= s < x2:
    #         ans += 1
    #         s, e = x1, x2
    # return ans

    # code refactoring 02 - 0.8675553719999999
    ans = 1
    targets.sort(reverse=True)
    s = targets[0][0]
    for x, y in targets:
        if y <= s:
            ans += 1
            s = x
    return ans


"""
(s,e) 구간에서 s와 e는 포격 불가 -> (s,e-1)로 계산

[1,4],[3,7],[4,5],[4,8],[5,12],[10,14],[11,13]
[11,13],[10,14],[5,12],[4,8],[4,5],[3,7],[1,4]

targets의 최소 교집합 구간을 찾아야 함 
1. targets 정렬
2. targets[-1] 구간과 겹치는 구간들 pop (요격)
3. target null 될 때까지 반복
4. 반복 횟수 반환
"""

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])) #3


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]],
        [[i, i+1] for i in range(1, 50001, 1)]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=100))
