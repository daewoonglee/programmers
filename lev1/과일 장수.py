def solution(k, m, score):
    score.sort(reverse=True)
    return sum([score[i] * m for i in range(m - 1, len(score), m)])


print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))
print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
