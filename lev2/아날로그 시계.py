
def solution(h1, m1, s1, h2, m2, s2):
    def time2sec(h, m, s):
        seconds = h*3600 + m*60 + s
        return seconds

    # 시분초를 초로 변환
    h1, m1, s1 = map(int, [h1, m1, s1])
    h2, m2, s2 = map(int, [h2, m2, s2])
    hms1 = time2sec(h1, m1, s1)
    hms2 = time2sec(h2, m2, s2)

    ans = 0
    # if hms1 == 0 or hms1 == 12 * 3600:
    #     ans += 1
    #
    # for sec in range(hms2-hms1):
    #     cur_s = s1 + sec  # 1초씩 증가
    #     cur_m = (m1 + cur_s / 60)  # 1초 증가할 때 0.x분 증가
    #     cur_h = (h1 + cur_m / 60) % 12 * 5  # 1초 증가할 때 0.x시간 증가
    #
    #     cur_s = cur_s % 60
    #     cur_m = cur_m % 60
    #     cur_h = cur_h % 60
    #
    #     next_s = (s1 + sec+1) # 1초씩 증가
    #     next_m = (m1 + (s1 + sec+1) / 60)  # 1초 증가할 때 0.x분 증가
    #     next_h = (h1 + next_m / 60) % 12 * 5  # 1초 증가할 때 0.x시간 증가
    #
    #     next_s = next_s % 60 if next_s % 60 != 0 else 60
    #     next_m = next_m % 60 if next_m % 60 != 0 else 60
    #     next_h = next_h if next_h % 60 != 0 else 60
    #
    #     if cur_s < cur_h and next_s >= next_h: ans += 1
    #     if cur_s < cur_m and next_s >= next_m: ans += 1
    #     if next_s == next_m == next_h: ans -= 1
    #     print(f"sec: {sec}, next h: {next_h}, m: {next_m}, s: {next_s}, cur h: {cur_h}, m: {cur_m}, s: {cur_s}, ans: {ans}")


    # code refactoring 02
    ans += int(hms2 / 3600 * 59)
    ans -= hms1 // (3600 / 59)
    ans += hms2 // (360 * 120 / 719)
    ans -= hms1 // (360 * 120 / 719)
    if hms1 <= 12 * 60 * 60 <= hms2: ans -= 1
    if hms1 == 0 or hms1 == 12 * 60 * 60: ans += 1

    return ans



# print(solution(0, 5, 30, 0, 7, 0)) # 2
# print(solution(12, 0, 0, 12, 0, 30)) # 1
# print(solution(0, 6, 1, 0, 6, 6)) # 0
print(solution(11, 59, 30, 12, 0, 0)) # 1
# print(solution(11, 58, 59, 11, 59, 0)) # 1
# print(solution(1, 5, 5, 1, 5, 6)) # 2
# print(solution(0, 0, 0, 23, 59, 59)) # 2852
# print(solution(1, 5, 0, 1, 5, 59)) # 2
#                                                                                       분침특이케이스     (시분초 겹치는순간)     시침 특이케이스
#                                                                      시간*60분*2,         59m-0m          00시, 12시        11-12, 23-0시
# print(solution(0, 0, 0, 1, 0, 0)) # 119         120                 -1              -1              0              118
# print(solution(0, 0, 0, 0, 1, 0)) # 1           2                   0               -1              0
# print(solution(1, 0, 0, 2, 0, 0)) # 119         120                 -1              -0              -0              119
# print(solution(11, 0, 0, 12, 0, 0)) # 118       120                 -1              -1              -1              117
# print(solution(11, 0, 0, 11, 59, 59)) # 117     118             X               X                   X           -> 59초가 돌면서 시/분침 만나는지 확인
