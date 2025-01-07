import sys
sys.setrecursionlimit(10000)


def solution(target):

    def countdown(q, d, t):
        nonlocal dart_cnt, single_bull
        if t < 0 or dart_cnt < q: return
        if t==0:
            print(f"q: {q}, dart_cnt: {dart_cnt}, d: {d}, singlebull: {single_bull}")
        if t == 0 and dart_cnt >= q:
            if dart_cnt == q and single_bull < d:
                single_bull = d
            elif dart_cnt != q:
                dart_cnt = q
                single_bull = d
            return

        range_li = [20, 19, 18, 17, 50, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for n in range_li:
            if n != 50:
                if n * 3 <= t:
                    countdown(q+1, d, t - n*3)
                elif n * 2 <= t:
                    countdown(q+1, d, t - n*2)
                elif n <= t:
                    countdown(q+1, d+1, t - n)
            elif n <= t:
                countdown(q+1, d+1, t - n)

    dart_cnt, single_bull = target, 0
    q, target = divmod(target, 300)
    print(q*5, target)
    countdown(q*5, 0, target)
    return [dart_cnt, single_bull]


    """
    shot = target
    ball_n_single = 0

    single = list(range(1, 21))
    
    def dfs(score, cnt, bs):
        '''
        score: 현재 점수
        cnt: 총 던진 횟수
        bs: 볼 또는 싱글을 맞춘 횟수
        '''
        nonlocal shot, ball_n_single

        # answer보다 더 많이 쐈으면 return
        if cnt > shot:
            return

        # 0점 밑으로 내려가면 return
        if score < 0:
            return

        # 0점이면 볼 또는 싱글 횟수 갱신
        if cnt <= shot and score == 0:
            if cnt == shot:
                ball_n_single = max(bs, ball_n_single)
            else:
                shot = cnt
                ball_n_single = bs

            return

        dfs(score - 50, cnt + 1, bs + 1)

        for s in single:
            if score - s < 0:
                break
            dfs(score - s, cnt + 1, bs + 1)
            dfs(score - s * 2, cnt + 1, bs)
            dfs(score - s * 3, cnt + 1, bs)

    dfs(target, 0, 0)
    
    return [shot, ball_n_single]
"""


# print(solution(21)) # [1,0]
# print(solution(58)) # [2,2]
# print(solution(100000)) # [1667, 0]
# print(solution(1)) # [1,1]
# print(solution(35)) #[2,2]
# print(solution(49)) #[2,1]
# print(solution(40)) #[1,0]
# print(solution(41)) #[2,1]
# print(solution(47)) #[2,1]
# print(solution(180)) #[3,0]
print(solution(250)) #[5,5]
# print(solution(103)) # [3,3]
# print(solution(102)) # [2,0]
# print(solution(101)) # [2,1]
# print(solution(117)) # [2,0]
# print(solution(160)) # [3,2]
# print(solution(147)) # [4,3]
# print(solution(191)) # [4,2]
# print(solution(247)) # [4,2]
# 141, 147 -> 3, 1
# 191, 197 -> 4, 2
# 241, 247 -> 5, 3
# print(solution(37)) # [2,2]
