from collections import Counter


def solution(weights):
    w_dict = Counter(weights)
    ans = 0
    for w, v in w_dict.items():
        if v > 1:
            ans += (v - 1) * v
        else:
            t = 0
            for i in range(2, 5):
                for j in range(2, 5):
                    if i != j and w * i // j in w_dict:
                        t += w_dict[w * i // j] if w_dict[w * i // j] == 1 else w_dict[w * i // j] * 2
            ans += t
    return ans // 2



"""
100:200=2:4
    2       3       4
2   a*2/2   a*2/3   a*2/4
3   a*3/2   a*3/3   a*3/4
4   a*4/2   a*4/3   a*4/4

    180 120 90
    270 180 135
    360 240 180
    
    270 180 135
    405 270 202
    540 360 270
    
    360 240 180
    540 360 270
    720 480 360
    
    100 66  55
    150 100 75
    200 133 100
    
    200 133 100
    300 200 150
    400 266 200
"""


# print(solution([100,180,360,100,270])) # 4
# print(solution([100,110])) # 0
# print(solution([100,100])) # 1
# print(solution([100,100,200])) # 3
# print(solution([100,100,100])) # 3
# print(solution([100,100,100,100])) # 6
print(solution([100,100,100,100,100])) # 10
print(solution([100,100,100,100,100,100])) # 15
print(solution([100,110,300,200])) # 2
