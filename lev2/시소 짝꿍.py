from collections import Counter


def solution(weights):
    w_dict = Counter(weights)
    ans = 0
    for w, v in w_dict.items():
        if v > 1:
            ans += (v - 1) * v
        # t = 0
        # for i in range(2, 5):
        #     for j in range(2, 5):
        #         if i != j and w * i // j in w_dict:
        #             t += w_dict[w * i // j] * v
        # ans += t
        ans += sum([w_dict[w*i//j]*v for i in range(2,5) for j in range(2,5) if i != j and w*i//j in w_dict])
    return ans // 2


print(solution([100,180,360,100,270])) # 4
print(solution([100,110])) # 0
print(solution([100,100])) # 1
print(solution([100,100,200])) # 3
print(solution([100,100,100])) # 3
print(solution([100,100,100,100])) # 6
print(solution([100,100,100,100,100])) # 10
print(solution([100,100,100,100,100,100])) # 15
print(solution([100,110,300,200])) # 2
print(solution([100,200,100,200,100,200])) # 15
