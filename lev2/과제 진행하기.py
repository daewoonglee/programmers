def solution(plans):
    def calc_task(t1, t2):
        if t1 > t2:
            t1 -= t2
            t2 = 0
        else:
            t2 -= t1
            t1 = 0
        return t1, t2

    def to_minute(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    # 0.569040446
    plans.sort(key=lambda x: x[1])

    ans = []
    task_list = []
    for (name, start, play_time) in plans:
        task_time = to_minute(start)
        play_time = int(play_time)

        if task_list:
            remain_time, task_list[-1][2] = calc_task(task_time - task_list[-1][1], task_list[-1][2])
            while remain_time >= 0 and task_list and task_list[-1][2] == 0:
                cur_task = task_list.pop()
                ans.append(cur_task[0])
                if task_list:
                    remain_time, task_list[-1][2] = calc_task(remain_time, task_list[-1][2])
        task_list.append([name, task_time, play_time])

    while task_list:
        ans.append(task_list.pop()[0])

    return ans


# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])) #["korean", "english", "math"]
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])) #["science", "history", "computer", "music"]
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])) #["bbb", "ccc", "aaa"]
# print(solution([["aa", "01:00", "15"], ["bb", "01:10", "15"], ["cc", "01:20", "30"], ["dd", "02:00", "10"]])) # ["cc, "bb", "aa", "dd"]
print(solution([["aa", "01:00", "40"], ["bb", "01:20", "10"], ["cc", "01:30", "10"], ["dd", "01:50","10"]])) # ["bb", "cc", "dd", "aa"]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]],
        [[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]],
        [[["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]],
        [[["aa", "01:00", "15"], ["bb", "01:10", "15"], ["cc", "01:20", "30"], ["dd", "02:00", "10"]]],
        [[["aa", "01:00", "40"], ["bb", "01:20", "10"], ["cc", "01:30", "10"], ["dd", "01:50","10"]]],
        [[["aa", "01:00", "40"], ["bb", "01:20", "10"], ["cc", "01:30", "10"], ["dd", "01:50", "10"], ["ee", "02:00", "40"], ["ff", "02:20", "10"], ["gg", "02:30", "10"], ["hh", "02:50", "10"], ["ii", "03:00", "40"], ["jj", "03:20", "10"], ["kk", "03:30", "10"], ["ll", "03:50", "10"], ["mm", "04:00", "40"], ["nn", "04:20", "10"], ["oo", "04:30", "10"], ["pp", "04:50", "10"]]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
