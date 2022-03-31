global_diff = 0
global_ans = []


def solution(n, info):
    def shoot(stack):
        global global_diff, global_ans
        while stack:
            arrows, idx, lion_score, appeach_score, li = stack.pop()
            if arrows == 0:
                if lion_score > appeach_score and (lion_score - appeach_score) > global_diff:
                    global_diff = (lion_score - appeach_score)
                    global_ans = li[:]
            else:
                if arrows < 0 or (arrows == n and len(li)-idx < arrows): continue
                if idx == len(li)-1:
                    li[-1] = arrows
                    stack.append([0, len(li)-1, lion_score, appeach_score, li])
                else:
                    li[idx] = info[idx]+1
                    stack.append([arrows-info[idx]-1, idx+1, lion_score+scores[idx], appeach_score-scores[idx] if info[idx] else appeach_score, li[:]])
                    li[idx] = 0
                    stack.append([arrows, idx+1, lion_score, appeach_score, li[:]])

    global global_ans
    scores = [i for i in range(10, -1, -1)]
    shoot([[n, 0, 0, sum([scores[i] for i, s in enumerate(info) if s]), [0]*11]])
    return global_ans if global_ans else [-1]


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])) # [1,1,1,1,1,1,1,1,0,0,2]

