def solution(sequence):
    # # 3.095602526
    # local_max = [[0] * (len(sequence)+1) for _ in range(2)]
    # pulse = 1
    # for i, s in enumerate(sequence):
    #     s *= pulse
    #     local_max[0][i] = max(local_max[0][i-1] + s, s)
    #     local_max[1][i] = max(local_max[1][i-1] + s * -1, s * -1)
    #     pulse *= -1
    # return max(max(local_max[0]), max(local_max[1]))

    # code refactoring - 1.1849952400000001
    # 구간합&누적합으로 접근
    # 위 접근 방식은 pulse가 [1,-1,1,...]이든 [-1,1,-1,...]이든 부호만 다르고 값은 동일하게 나옴
    prefix_sum = [0]
    pulse = 1
    for i, s in enumerate(sequence):
        s *= pulse
        prefix_sum.append(prefix_sum[-1] + s)
        pulse *= -1
    # print(prefix_sum)
    return max(prefix_sum) - min(prefix_sum)


"""
[2, 3, -6,   1, 3,  -1, 2,  4]
2   -3  -6   -1   3  1   2   -4
-2  3   6   1  -3   -1  -2   4

DP, Kadane's algorithm
2   -1  -6  -1  3   4   6   2
-2  3   9   10  7   6   4   8
"""

# print(solution([2, 3, -6, 1, 3, -1, 2, 4])) #10
# print(solution([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])) #10
# print(solution([1,2,3,4,5,6,7,8,9,10])) #10
print(solution([-30, 2])) #32
print(solution([-10, 1, -10])) #21

if __name__ == "__main__":
    from timeit import Timer
    query = [
        [2, 3, -6, 1, 3, -1, 2, 4],
        [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [i for i in range(50000)]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=100))
