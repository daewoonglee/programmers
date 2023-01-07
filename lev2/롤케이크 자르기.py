def solution(topping):
    ans = 0
    piece1 = set()
    piece2 = set(topping[1:])
    for i, t in enumerate(topping[:-1]):
        piece1.add(t)
        piece2 = set(topping[i+1:])
        if len(piece1) == len(piece2):
            ans += 1
    return ans


print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0
print(solution([1])) # 0
