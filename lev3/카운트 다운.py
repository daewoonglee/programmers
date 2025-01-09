import sys
sys.setrecursionlimit(10000)


def solution(target):

    def countdown(s, sb, t):
        nonlocal dart_cnt, single_bull
        if dart_cnt < s: return
        if t == 0:
            if dart_cnt == s:
                if single_bull < sb:
                    single_bull = sb
            else:
                dart_cnt = s
                single_bull = sb
            return

        range_li = [20, 19, 18, 17, 50, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for n in range_li:
            # print(f"n: {n}, dart_cnt: {dart_cnt}, singlenbull: {single_bull}, target: {t}")
            if n != 50:
                if n * 3 <= t:
                    countdown(s+1, sb, t - n*3)
                elif n * 2 <= t:
                    countdown(s+1, sb, t - n*2)
                elif n <= t:
                    countdown(s+1, sb+1, t - n)
            elif n <= t:
                countdown(s+1, sb+1, t - n)

    dart_cnt, single_bull = target, 0
    if target > 310:
        shot = (target-310) // 60 + 1
        target -= 60*shot
    else:
        shot = 0
    countdown(shot, 0, target)
    return [dart_cnt, single_bull]


# print(solution(21)) # [1,0]
# print(solution(58)) # [2,2]
# print(solution(100000)) # [1667, 2]
# print(solution(1)) # [1,1]
# print(solution(35)) #[2,2]
# print(solution(49)) #[2,1]
# print(solution(40)) #[1,0]
# print(solution(41)) #[2,1]
# print(solution(47)) #[2,1]
# print(solution(180)) #[3,0]
# print(solution(250)) #[5,5]
# print(solution(103)) # [3,3]
# print(solution(102)) # [2,0]
# print(solution(101)) # [2,1]
# print(solution(117)) # [2,0]
# print(solution(160)) # [3,2]
# print(solution(147)) # [3,1]
# print(solution(191)) # [4,2]
print(solution(310)) # [6,5] <-
# print(solution(247)) # [5,3] // 57, 50,50,50, 40
# print(solution(547)) # [10,5] // 57, 50,50,50, 40, 60,60,60,60
