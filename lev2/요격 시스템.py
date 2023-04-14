def solution(targets):
    ans = 0
    targets.sort()
    while targets:
        s, e = targets.pop()
        while targets and targets[-1][0] <= s < targets[-1][1]:
            targets.pop()
        ans += 1
    return ans


"""
(s,e) 구간에서 s와 e는 포격 불가 -> (s,e-1)로 계산

[1,4],[3,7],[4,5],[4,8],[5,12],[10,14],[11,13]

targets의 최소 교집합 구간을 찾아야 함 
1. targets 정렬
2. targets[-1] 구간과 겹치는 구간들 pop (요격)
3. target null 될 때까지 반복
4. 반복 횟수 반환
"""

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])) #3
