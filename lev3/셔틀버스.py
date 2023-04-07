def datetime_to_min(time_hm):
    h, m = map(int, time_hm.split(":"))
    return h * 60 + m


def min_to_datetime(time_min):
    q, d = time_min // 60, time_min % 60
    return f"{str(q).zfill(2)}:{str(d).zfill(2)}"


def solution(n, t, m, timetable):
    # 0.55701053
    timetable.sort(reverse=True)

    for i in range(n): # 0 < n이기 때문에 for loop는 반드시 구동 (waiting_line, bus_time 변수는 반드시 존재)
        cnt = 0
        waiting_line = []
        bus_time = 9 * 60 + i * t
        while timetable and datetime_to_min(timetable[-1]) <= bus_time and cnt < m:
            waiting_line.append(timetable.pop())
            cnt += 1

    return min_to_datetime(bus_time) if len(waiting_line) < m else min_to_datetime(datetime_to_min(waiting_line[-1])-1)


# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])) #"09:00"
# print(solution(2,10,2,["09:10", "09:09", "08:00"])) #"09:09"
# print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])) #"08:59"
# print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])) #"00:00"
# print(solution(1,1,1,["23:59"])) #"09:00"
# print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])) #"18:00"
print(solution(3,10,3,["09:00", "09:00", "09:00", "09:10", "09:10", "09:10", "09:20", "09:20", "09:20", "09:20"])) #"09:19"


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [1,1,5,["08:00", "08:01", "08:02", "08:03"]],
        [2,10,2,["09:10", "09:09", "08:00"]],
        [2,1,2,["09:00", "09:00", "09:00", "09:00"]],
        [1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]],
        [1,1,1,["23:59"]],
        [10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]],
        [3,10,3,["09:00", "09:00", "09:00", "09:10", "09:10", "09:10", "09:20", "09:20", "09:20", "09:20"]],
        [10,60,45,["09:00"]*2000]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
