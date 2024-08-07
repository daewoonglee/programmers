def solution(scores):
    print(f"origin scores: {scores}")
    for i, score in enumerate(scores):
        score.append(i)
    scores.sort(key=lambda x: [x[0], x[1]])

    total_scores = []
    for score1, score2, idx in scores:
        total_scores.append([score1+score2, idx])
    print(f"sorting scores: {scores}")
    print(f"total_scores: {total_scores}")

    for i, (score1, score2, idx) in enumerate(scores):
        for j in range(i+1, len(scores)):
            if score1 != scores[j][0] and score2 < scores[j][1]:
                total_scores[i][0] = -1
                break
    print(f"-1 total_scores: {total_scores}")

    total_scores.sort(key=lambda x: x[0], reverse=True)
    print(f"sorting total_scores: {total_scores}")

    ans = 1
    cnt = 0
    for i, total_score in enumerate(total_scores):
        print(f"i: {i}, ans: {ans}, cnt: {cnt}, total_socre: {total_score}, total_score[-1]: {total_score[-1]}")
        if total_score[-1] == 0:
            if total_score[0] == -1:
                ans = -1
            break
        cnt += 1
        if i < len(total_scores) and total_score[0] != total_scores[i+1][0]:
            ans += cnt
            cnt = 0
    print(f"ans: {ans}")
    return ans



"""
sum 한 값 sorting (오름차순)
여기서 다른 임의의 사원보다 점수가 모두 낮은 경우를 제외
같은 값을 가지면 등수는 동일하고 그 수만틈 석처를 건너뜀
[0] 인덱스 완호가 몇등인지 반환
"""

# print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) # 4
# print(solution([[2,2],[2,4],[2,2],[2,3],[2,1],[2,2]])) # 3
# print(solution([[2,1],[1,2],[1,2],[1,2],[1,1],[1,2],[1,2]])) # 1
print(solution([[0,0],[1,2],[2,1],[1,2],[1,1],[1,2],[1,2]])) # 1
