def solution(plans):
    def calc_task(t1, t2):
        if t1 > t2:
            t1 -= t2
            t2 = 0
        else:
            t2 -= t1
            t1 = 0
        return t1, t2

    plans.sort(key=lambda x: x[1])
    print(plans)

    ans = []
    task_list = []
    for (name, start, play_time) in plans:
        h, m = map(int, start.split(":"))
        task_time = h*60+m
        play_time = int(play_time)
        if task_list:
            remain_time, task_list[-1][2] = calc_task(task_time - task_list[-1][1], task_list[-1][2])
            while remain_time >= 0 and task_list and task_list[-1][2] <= 0:
                cur_task = task_list.pop()
                ans.append(cur_task[0])
                if task_list:
                    remain_time, task_list[-1][2] = calc_task(remain_time, task_list[-1][2])
        task_list.append([name, task_time, play_time])

    while task_list:
        ans.append(task_list.pop()[0])

    return ans

"""
1. sort 시작 시간대가 빠른 순서
2. stack 자료구조로 데이터 보관 & 과제 남은 시간 계산 (하나의 과제를 여러번 진행했던 멈출 수 있음)

3. stack[-1]의 필요시간과 다음 리스트 시작 시간 비교
 3-1.
    if stack[-1]_remain_time < next_time
        stack.pop
        남은 시간 계산
        loop stack
            stack[-1]_remain_time에서 남은 시간만큼 과제 필요시간 차감
    else stack.append
시간대 계산을 어떻게 진행할 것인가 ? -> 시간대를 모두 분으로 환산하여 계산

["music", "12:20", "40"],["computer", "12:30", "100"],["science", "12:40", "50"],["history", "14:00", "30"]
["music", "720", "40"], ["computer", "750", "100"], ["science", "760", "50"], ["history", "840", "30"]
"""

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])) #["korean", "english", "math"]
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])) #["science", "history", "computer", "music"]
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])) #["bbb", "ccc", "aaa"]
# print(solution([["aa", "01:00", "15"], ["bb", "01:10", "15"], ["cc", "01:20", "30"], ["dd", "02:00", "10"]])) # ["cc, "bb", "aa", "dd"]
print(solution([["aa", "01:00", "40"], ["bb", "01:20", "10"], ["cc", "01:30", "10"], ["dd", "01:50","10"]])) # ["bb", "cc", "dd", "aa"]
