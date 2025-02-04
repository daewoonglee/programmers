def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    ans = []
    while left < right:
        level = (right + left) // 2
        pre_time = 0
        play_time = 0
        for i, d in enumerate(diffs):
            cur_time = times[i]
            play_time += (cur_time + pre_time) * (d-level) + cur_time if d > level else cur_time
            pre_time = cur_time

        if play_time <= limit:
            ans.append(level)
            right = level
        else:
            if left == level:
                break
            left = level
    return min(ans) if ans else right


# print(solution([1, 5, 3], [2, 4, 7], 30)) # 3
# print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59)) # 2
# print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)) # 294
# print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)) # 39354
# print(solution([1], [1], 10)) # 1
# print(solution([10], [1], 1)) # 10
print(solution([1, 5], [10000, 10000], 20000)) # 5
