def solution(n, info):
    scores = [i for i in range(10, -1, -1)]
    appeach_score = sum([scores[i] for i in info if i])
    global_score = 0
    global_ans = [0] * 10
    print(global_ans)
    for i in range(10):
        arrows = n - info[i] - 1
        if arrows < 0: break
        challenger = appeach_score - scores[i]
        local_score = scores[i]
        local_ans = [0] * 10
        local_ans[i] = info[i]+1
        for j in range(i+1, 10): # 재귀처리 필요
            arrows -= (info[j]+1)
            if arrows < 0: break
            challenger -= scores[j]
            local_score += scores[j]
            local_ans[j] = info[j]+1
        if local_score > global_score and local_score > challenger:
            global_score = local_score
            global_ans = local_ans[:]
        return global_score, global_ans

    return global_ans if global_ans else [-1]


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))

