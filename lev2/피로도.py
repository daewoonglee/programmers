from itertools import permutations


def solution(k, dungeons):
    global_ans = 0
    for p_dungeons in permutations(dungeons, len(dungeons)):
        ans = 0
        N = k
        for d in p_dungeons:
            if N >= d[0]:
                ans += 1
                N -= d[1]
        if global_ans < ans:
            global_ans = ans
    return global_ans
    

print(solution(80, [[80,20], [50,40], [30,10]]))
print(solution(100, [[10,10], [20,20], [30,30], [40,10]]))
