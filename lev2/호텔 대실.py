def solution(book_time):
    cleaning_time = 9 # 10분 이후부턴 사용 가능
    book_time.sort(key=lambda x: x[0])

    short_stay = []
    for bt in book_time:
        sh, sm = map(int, bt[0].split(":"))
        eh, em = map(int, bt[1].split(":"))
        for i, check_out in enumerate(short_stay):
            if check_out < sh*60+sm:
                short_stay[i] = eh*60 + em + cleaning_time
                break
        else:
            short_stay.append(eh*60 + em + cleaning_time)

    return len(short_stay)


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["10:19", "12:20"]])) # 2
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3
print(solution([["08:20", "09:30"]])) # 1
print(solution([["08:20", "09:30"]]*1000)) # 1000
print(solution([["00:20", "01:30"], ["01:40", "02:30"], ["02:39", "03:30"]])) # 2
