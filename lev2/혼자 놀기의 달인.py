def solution(cards):
    ans = []
    pts = 0
    for i in range(len(cards)):
        cnt = 0
        while cards[pts]:
            cnt += 1
            temp = cards[pts]
            cards[pts] = 0
            pts = temp - 1
        if cnt: ans.append(cnt)
        pts = i-1

    ans.sort()
    return 0 if len(ans) < 2 else ans[-1] * ans[-2]


print(solution([8,6,3,7,2,5,1,4])) # 12
print(solution([2,1])) # 0
