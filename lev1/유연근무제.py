from datetime import datetime, timedelta


def solution(schedules, timelogs, startday):
    ans = 0
    startday -= 1
    for s, time_log in zip(schedules, timelogs):
        s = datetime.strptime(f"{s//100}:{s%100}", "%H:%M") + timedelta(minutes=10)
        for i, t in enumerate(time_log):
            if (i+startday) % 7 in [5, 6]: continue
            elif datetime.strptime(f"{t//100}:{t%100}", "%H:%M") > s: break
        else:
            ans += 1
    return ans


print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001,1100]], 5)) # 3
print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1)) # 2
