def solution(h1, m1, s1, h2, m2, s2):
    def time2sec(h, m, s):
        seconds = h*3600 + m*60 + s
        return seconds

    # 시분초를 초로 변환
    h1, m1, s1 = map(int, [h1, m1, s1])
    h2, m2, s2 = map(int, [h2, m2, s2])
    hms1 = time2sec(h1, m1, s1)
    hms2 = time2sec(h2, m2, s2)
    print(f"h1: {h1}, m1: {m1}, s1: {s1}")

    ans = 0
    pre_sec, pre_min, pre_hour = s1, m1, h1
    for sec in range(hms2-hms1+1):
        s = (s1 + sec)  # 1초씩 증가
        m = (m1 + s / 60)  # 1초 증가할 때 0.x분 증가
        h = (h1 + m / 60) % 12 * 5 # 1초 증가할 때 0.x시간 증가

        s %= 60 # 정각 지나는 경우
        m %= 60 # 정각 지나는 경우

        if m == h: ans += 1 # 시/분침이 겹치는 경우
        else:
            if pre_sec < m <= (s if s != 0 else 60): ans += 1
            if pre_sec < h <= (s if s != 0 else 60): ans += 1
            if pre_min == pre_hour: ans -= 2 # 시/분침이 겹친 상태에서 시작한 경우, 위 if문 2개가 참이라서
        print(f"sec: {sec}, h: {h}, m: {m}, s: {s}, ans: {ans}")
        pre_sec = s
        pre_min = m
        pre_hour = h

    return ans

# print(solution(0, 5, 30, 0, 7, 0)) # 2
# print(solution(12, 0, 0, 12, 0, 30)) # 1
# print(solution(0, 6, 1, 0, 6, 6)) # 0
# print(solution(11, 59, 30, 12, 0, 0)) # 1
# print(solution(11, 58, 59, 11, 59, 0)) # 1
# print(solution(1, 5, 5, 1, 5, 6)) # 2
print(solution(0, 0, 0, 23, 59, 59)) # 2852
