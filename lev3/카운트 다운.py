
def solution(target):
    def update_dp(t_num, add_shot):
        add_dart, add_single_bull = DP[add_shot]
        dart, single_bull = DP[t_num - add_shot]
        if add_dart + dart < DP[t_num][0]:
            DP[t_num] = [add_dart + dart, add_single_bull + single_bull]
        elif add_dart + dart == DP[t_num][0] and add_single_bull + single_bull > DP[t_num][1]:
            DP[t_num][1] = add_single_bull + single_bull

    def countdown(target_num):
        dart_li = list(range(1, 21)) + [50]
        for t in range(21, target_num+1):
            for n in dart_li:
                if n != 50:
                    for k in range(1, 4): # single, double, triple
                        if t > n*k:
                            update_dp(t, n*k)
                else:
                    if t > n:
                        update_dp(t, n)

    DP = [[100000, 0] for _ in range(100001)]  # 숫자=배열인덱스로 맞춤
    for i in range(21):
        DP[i] = [1, 1]
        DP[i * 2] = [1, 0]
        DP[i * 3] = [1, 0]
    DP[50] = [1, 1]

    countdown(target)
    return [DP[target][0], DP[target][1]]


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
print(solution(247)) # [5,3] // 57, 50,50,50, 40
print(solution(547)) # [10,5] // 57, 50,50,50, 40, 60,60,60,60
