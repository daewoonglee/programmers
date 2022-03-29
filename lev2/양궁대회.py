global_score = 0
global_ans = []


def solution(n, info):
    def shoot(stack):
        global global_score, global_ans
        while stack:
            arrows, idx, score, li = stack.pop()
            if arrows - (info[idx]+1) >= 0:
                if idx == len(li)-1: continue
                li[idx] = info[idx]+1
                stack.append([arrows-info[idx]-1, idx+1, score+scores[idx], li[:]])
                li[idx] = 0
                stack.append([arrows, idx+1, score, li[:]])
            else:
                if score > global_score:
                    global_score = score
                    global_ans = li[:]
        shoot(stack)

    scores = [i for i in range(10, -1, -1)]
    shoot([[n, 0, 0, [0]*10]])
    return global_ans if sum([scores[i] for i, s in enumerate(info) if s]) - global_ans *2 < 0 else [-1]


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]

