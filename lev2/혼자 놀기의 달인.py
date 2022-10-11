def solution(cards):
    ans = []
    idx = 0
    pts = 0
    N = len(cards)
    while idx < N:
        cnt = 0
        while cards[pts]:
            cnt += 1
            temp = cards[pts]
            cards[pts] = 0
            pts = temp-1
        idx += 1
        ans.append(cnt)
        pts = idx-1
    print(ans)
    ans.sort()
    if not ans: return 0
    elif len(ans) > 1: return ans[-1] * ans[-2]
    else: return ans


print(solution([8,6,3,7,2,5,1,4]))
