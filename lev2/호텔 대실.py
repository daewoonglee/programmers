def solution(book_time):
    cleaning_time = 9 # 10분 이후부턴 사용 가능
    book_time.sort(key=lambda x: x[0])
    print(f"sorted book: {book_time}")

    short_stay = []
    for bt in book_time:
        next_time = int(bt[0].replace(":", ""))
        for i, ss in enumerate(short_stay):
            if ss < next_time:
                short_stay[i] = int(bt[-1].replace(":", "")) + cleaning_time
                break
        else:
            short_stay.append(int(bt[-1].replace(":", "")) + cleaning_time)
    print(f"stay: {short_stay}")
    return len(short_stay)

"""
["14:10", "19:20"], ["14:20", "15:20"], ["15:00", "17:00"], ["16:40", "18:20"], ["18:20", "21:20"]

short_stay
14:10----------------------------19:29
 14:20---15:29  16:40------18:29
       15:00-------16:59  18:20-----------------21:29
       
if short_stay[i][-1] > book_time[j][0] # 대실중이라면
    short_stay.append(book_time[j][0])
else
    short_stay[i] = book_time[j][-1] 
"""


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["10:19", "12:20"]])) # 2
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3
