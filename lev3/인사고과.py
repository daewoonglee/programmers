def solution(scores):
    target1, target2 = scores[0]
    target = target1 + target2

    scores.sort(key=lambda x: [-x[0], x[1]])
    ans = 1
    max_b = 0
    for i, (score1, score2) in enumerate(scores):
        if target1 < score1 and target2 < score2: return -1

        if score2 >= max_b:
            max_b = score2
            if score1+score2 > target:
                ans += 1

    return ans


# print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) # 4
# print(solution([[2,2],[2,4],[2,2],[2,3],[2,1],[2,2]])) # 3
# print(solution([[0,3],[1,2],[1,2],[1,2],[1,1],[1,2],[1,2]])) # 1
# print(solution([[0,0],[1,2],[2,1],[1,2],[1,1],[1,2],[1,2]])) # -1
print(solution([[1,1],[4,0],[0,4],[1,3],[2,1],[3,1],[1,2],[0,3],[1,2],[0,0],[0,0],[2,0]])) # 9
# print(solution([[1,1],[4,0],[0,4],[1,2],[0,3],[2,2],[2,0],[0,2]])) # -1

