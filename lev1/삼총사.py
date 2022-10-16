from itertools import combinations


def solution(number):
    return [sum(c) for c in combinations(number, 3)].count(0)


# print(solution([-2, 3, 0, 2, -5])) # 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 5
# print(solution([-1, 1, -1, 1])) # 0
print(solution([1, -1, 0])) # 1
