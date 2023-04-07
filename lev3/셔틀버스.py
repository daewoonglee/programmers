def datetime_to_min(time_hm):
    h, m = map(int, time_hm.split(":"))
    return h * 60 + m


def min_to_datetime(time_min):
    q, d = time_min // 60, time_min % 60
    return f"{str(q).zfill(2)}:{str(d).zfill(2)}"


def solution(n, t, m, timetable):
    timetable.sort(reverse=True)
    timetable = [datetime_to_min(tt) for tt in timetable]

    bus_time = 9 * 60
    for _ in range(n): # 0 < n이기 때문에 for loop는 반드시 구동 (waiting_line 변수는 반드시 존재하게 됨)
        cnt = 0
        waiting_line = []
        while timetable and timetable[-1] <= bus_time and cnt < m:
            waiting_line.append(timetable.pop())
            cnt += 1
        bus_time += t

    print(waiting_line)
    return min_to_datetime(9 * 60 + (n-1) * t) if len(waiting_line) < m else min_to_datetime(waiting_line[-1]-1)


"""
가장 늦게 출발하는 셔틀 타기

1. 09:00 기준부터 셔틀 출발하니깐 주어진 N & t 기준으로 갈 수 있는 가장 늦은 셔틀 시간대 계산
    - last_shuttle_bus = 09 * 60 + (n-1) * t (계산 편의를 위해 분 단위로 환산)
2. sort timetable
3. 막차 시간까지 대기열 & 현재 시간 갱신
    - loop n만큼
        while timetable[i] < t시 & len(list) < m -> list append timetable[i]
        else -> t += 1 & init list    
4. 막차 시간에 대기열 탑승 가능 인원
    if 탑승 인원 < m -> 막차 시간 반환
    else -> 탑승 인원 리스트[m-1]-1 시간 반환
"""


# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])) #"09:00"
# print(solution(2,10,2,["09:10", "09:09", "08:00"])) #"09:09"
# print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])) #"08:59"
# print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])) #"00:00"
# print(solution(1,1,1,["23:59"])) #"09:00"
# print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])) #"18:00"
print(solution(3,10,3,["09:00", "09:00", "09:00", "09:10", "09:10", "09:10", "09:20", "09:20", "09:20", "09:20"])) #"09:19"
