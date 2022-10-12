def solution(cards):
    # 0.27821902499999995
    ans = []
    for i in range(len(cards)):
        cnt = 0
        pts = i
        while cards[pts]:
            cnt += 1
            temp = cards[pts]
            cards[pts] = 0
            pts = temp - 1
        if cnt: ans.append(cnt)
    ans.sort()
    return 0 if len(ans) < 2 else ans[-1] * ans[-2]


print(solution([8,6,3,7,2,5,1,4])) # 12
print(solution([2,1])) # 0


if __name__ == "__main__":
    from timeit import Timer
    import random
    r = [i for i in range(1, 101)]
    r1 = r[:50]
    random.shuffle(r)
    random.shuffle(r1)
    query = [[8,6,3,7,2,5,1,4], [2,1], r, r1]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
