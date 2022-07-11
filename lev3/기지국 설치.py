import math
def solution(n, stations, w):
    ans = 0
    apart = [0] * n
    step = w*2+1
    for s in stations:
        for i in range(s-w-1, s+w):
            if 0 <= i < n: apart[i] = 1
    print(f"log: {apart}")

    pre, idx = -1, 0
    while idx < n:
        if apart[idx] == 0:
            if pre == -1: pre = idx
        else:
            if pre != -1:
                print(f"ans: {ans}, idx: {idx}, pre: {pre}, step: {step}, sum: {((idx-pre) // step + 1)}, //: {(idx-pre)/step}, ceil: {math.ceil((idx-pre)/step)}")
                # ans += ((idx-pre) // step + 1)
                ans += (math.ceil((idx-pre) / step))
                for i in range(pre, idx):
                    apart[i] = 1
                    # print(f"pre: {pre}, idx: {idx}, i: {i}")
                pre = -1
        idx += 1

    print(f"ans: {ans}, idx: {idx}, pre: {pre}, step: {step}, sum: {((idx-pre) // step + 1)}")
    # if pre != -1: ans += ((idx-pre) // step + 1)
    if pre != -1: ans += (math.ceil((idx-pre) / step))

    return ans


# print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))

