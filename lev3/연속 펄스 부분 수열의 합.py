def solution(sequence):
    local_max = [[0] * len(sequence) for _ in range(2)]
    local_max[0][0] = sequence[0]
    local_max[1][0] = -sequence[0]
    pulse = -1
    for i in range(1, len(sequence)):
        s = sequence[i] * pulse
        local_max[0][i] = max(local_max[0][i-1] + s, s)
        local_max[1][i] = max(local_max[1][i-1] + s * -1, s * -1)
        pulse *= -1
    for lm in local_max:
        print(lm)
    return max(max(local_max[0]), max(local_max[1]))


"""
[2, 3, -6,   1, 3,  -1, 2,  4]
2   -3  -6   -1   3  1   2   -4
-2  3   6   1  -3   -1  -2   4

DP, Kadane's algorithm
2   -1  -6  -1  3   4   6   2
-2  3   9   10  7   6   4   8
"""

# print(solution([2, 3, -6, 1, 3, -1, 2, 4])) #10
print(solution([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])) #10
print(solution([1,2,3,4,5,6,7,8,9,10])) #10
