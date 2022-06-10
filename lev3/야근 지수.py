def solution(n, works):
    if sum(works) <= n: return 0
    # ver01
    # works.sort(reverse=True)
    for _ in range(n):
        # works[0] -= 1
        # if works[0] < works[1]:
        #     works.sort(reverse=True)

        # ver02
        works[works.index(max(works))] -= 1
    return sum([w*w for w in works])


# print(solution(4,[4,3,3])) # 12
# print(solution(1,[2,1,2])) # 6
# print(solution(3,[1,1]))   # 0
# print(solution(7,[10,9,3,3,3])) # 99
print(solution(99,[2,15,22,55,55])) # 580
# 2 12 12 12 12
#99, [2, 15, 22, 55, 55], 580
