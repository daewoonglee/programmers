from itertools import combinations


def solution(number):
    # 0.630136517
    # return [sum(c) for c in combinations(number, 3)].count(0)

    # 0.8106217960000001 - 패키지 없이 구현
    ans = 0
    N = len(number)
    for i in range(N):
        for j in range(i+1, N):
            n = number[i] + number[j]
            for z in range(j+1, N):
                if n + number[z] == 0: ans += 1
    return ans


# print(solution([-2, 3, 0, 2, -5])) # 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 5
# print(solution([-1, 1, -1, 1])) # 0
print(solution([1, -1, 0])) # 1


if __name__ == "__main__":
    from timeit import Timer
    query = [[-2, 3, 0, 2, -5],
             [-3, -2, -1, 0, 1, 2, 3],
             [-1, 1, -1, 1],
             [1, -1, 0],
             [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6],
             [1,2,3,4,5,6,7,8,9,10,11,12,13]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
