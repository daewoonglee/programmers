from collections import Counter


def solution(topping):
    ans = 0
    cnt_dic = Counter(topping)
    piece1 = set()
    piece2 = len(cnt_dic)
    for i, t in enumerate(topping[:-1]):
        piece1.add(t)
        cnt_dic[t] -= 1
        if cnt_dic[t] == 0:
            piece2 -= 1
        if len(piece1) == piece2: ans += 1
    return ans


print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0
print(solution([1, 2, 3, 4])) # 1
print(solution([1])) # 0
