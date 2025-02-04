def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    while left <= right:
        level = (left + right) >> 1
        play_time = 0
        for i, d in enumerate(diffs):
            play_time += (times[i-1] + times[i]) * (d-level) + times[i] if d > level else times[i]

        if play_time <= limit:
            right = level-1
        else:
            left = level+1
    return left


# print(solution([1, 5, 3], [2, 4, 7], 30)) # 3
# print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59)) # 2
# print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)) # 294
# print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)) # 39354
# print(solution([1], [1], 10)) # 1
# print(solution([10], [1], 1)) # 10
print(solution([1, 5], [10000, 10000], 20000)) # 5
