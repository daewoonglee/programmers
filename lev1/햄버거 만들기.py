def solution(ingredient):
    ans = 0
    packing = [[i, igd] for i, igd in enumerate(ingredient[:3])]
    idx = 3
    N = len(ingredient)-1
    while 0 <= idx < N:
        if packing[0][1] == 1 and packing[1][1] == 2 and packing[2][1] == 3:
            for j, _ in packing[::-1]:
                ingredient.pop(j)
            idx -= 3
            N -= 3
            packing = [[idx+i, igd] for i, igd in enumerate(ingredient[idx:idx+3])]
            ans += 1
        else:
            packing[0] = packing[1]
            packing[1] = packing[2]
            packing[2] = [idx, ingredient[idx]]
        idx += 1
    return ans


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
print(solution([1, 2, 1, 2, 3, 1, 2, 3, 3])) # 3

