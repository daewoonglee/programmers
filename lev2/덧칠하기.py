def solution(n, m, section):
    ans = 0
    step = 0
    for s in section:
        if step < s:
            step = m + s - 1
            ans += 1
    return ans


"""
주어진 섹터에서 롤러 길이로 최대한 많이 칠할 수 있는 벽의 위치를 탐색하여 칠함(ans+1)
이후 남은 섹터에서 롤러 길이로 최대한 많이 칠할 수 있는 위치를 탐색하여 칠함 (반복)
"""

print(solution(8, 4, [2, 3, 6])) # 2
print(solution(5, 4, [1, 3])) # 1
print(solution(4, 1, [1, 2, 3, 4])) # 4
print(solution(20, 4, [1, 4, 5, 6, 7, 12, 14, 15])) # 3
