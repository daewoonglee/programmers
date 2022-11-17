def solution(k, m, score):
    score.sort()
    ans = 0
    for i in range(1, len(score)//m+1):
        if i == 0: i += 1
        ans += min(score[i: i*m]) * m
    return ans


print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))
print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
