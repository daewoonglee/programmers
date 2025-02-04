import math


def solution(diffs, times, limit):
    level = 0
    play_time = 0
    pre_time = 0
    temp = 0
    for i, d in enumerate(diffs):
        cur_time = times[i]
        play_time += (cur_time + pre_time) * (d - level) + cur_time if d > level else cur_time
        temp += (cur_time + pre_time) * (d-level-1) + cur_time if d > level else cur_time
        pre_time = cur_time
    step = play_time - temp

    min_diffs = [0] + sorted(diffs)
    idx = 1
    print(f"min: {min_diffs}, ")
    print(f"level: {level}, puzzle play_time: {play_time}, step: {step}, temp: {temp}, value: {play_time - step * (min_diffs[idx] - level)}")

    # giant step
    while not play_time - step * (min_diffs[idx] - min_diffs[idx-1]) <= limit:
        play_time -= (min_diffs[idx]-min_diffs[idx-1])*step
        level = min_diffs[idx]+1
        pre_time = 0
        temp = 0
        for i, d in enumerate(diffs):
            cur_time = times[i]
            temp += (cur_time + pre_time) * (d-level) + cur_time if d > level else cur_time
            pre_time = cur_time

        step = play_time - temp
        idx += 1
        print(f"level: {level}, puzzle: {play_time}, step: {step}, temp: {temp}, value: {play_time - step * (min_diffs[idx] - min_diffs[idx-1])}")

    # baby step
    print(f"plus step: {math.ceil((-limit+temp) / step)}, v: {(-limit+temp) / step}")
    return level + math.ceil((-limit+temp) / step)


# print(solution([1, 5, 3], [2, 4, 7], 30)) # 3
# print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59)) # 2
# print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)) # 294
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)) # 39354