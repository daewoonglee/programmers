def solution(ingredient):
    ans = 0
    packing = [[i, igd] for i, igd in enumerate(ingredient[:3])]
    idx = 2
    N = len(ingredient)-1
    while 0 <= idx < N:
        print(f"idx: {idx}, pack; {packing}, igds: {ingredient}, N: {N}")
        if packing[0][1] == 1 and packing[1][1] == 2 and packing[2][1] == 3:
            for j, _ in packing[::-1]: ingredient.pop(j)
            idx -= (5 if idx > 5 else idx)
            N -= 3
            packing = [[idx+i, igd] for i, igd in enumerate(ingredient[idx:idx+3])]
            ans += 1
        else:
            idx += 1
            packing[0] = packing[1]
            packing[1] = packing[2]
            packing[2] = [idx, ingredient[idx]]
    print(f"after idx: {idx}, pack; {packing}, igds: {ingredient}, N: {N}, ans: {ans}")
    return ans


# print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
# print(solution([1, 2, 1, 2, 3, 1, 2, 3, 3])) # 3
# print(solution([1, 1, 2, 1, 2, 3, 3, 2, 3, 3])) # 3
print(solution([1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 2, 3, 3, 1, 2, 3, 3, 3, 3, 3])) # 5
print(solution([1, 2, 3] * 100)) # 5
print(solution([1, 1, 2, 1, 2, 1, 2, 3, 3, 3, 2, 3])) # 4
print(solution([1, 1, 1, 2, 3, 2, 3, 2, 3])) # 3
