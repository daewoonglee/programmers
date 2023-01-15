def solution(storey):
    # # 0.239197214 - convert str
    # ans = 0
    # rnd = 0
    # storey = str(storey)[::-1]
    # for i, n in enumerate(storey):
    #     q = (int(n) + rnd)
    #     if q >= 5: # up
    #         ans += 10-q
    #         # 5 자릿수 앞에 0~4이거나 5앞에 수가 없으면 0(down) 그렇지 않으면 1(up)
    #         rnd = 0 if q == 5 and (i+1 == len(storey) or int(storey[i+1]) < 5) else 1
    #     else: # down
    #         ans += q
    #         rnd = 0
    #     # print(f"q: {q}, rnd: {rnd}, ans: {ans}")
    # return ans + rnd

    # code refactoring - # 0.107456529
    ans = 0
    while storey > 0:
        storey, n = divmod(storey, 10)
        if n >= 5: # up
            ans += 10-n
            if not (n == 5 and storey % 10 < 5):
                storey += 1
        else: # down
            ans += n
    return ans


print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(2054)) # 11

print(solution(44)) # 8 (down)
print(solution(45)) # 9 (down)
print(solution(46)) # 9 (up)

print(solution(54)) # 9 (down)
print(solution(55)) # 10 (up || down)
print(solution(56)) # 9 (up)

print(solution(455)) # 14 (up)
print(solution(555)) # 14 (up)

print(solution(64)) # 9 (down)
print(solution(65)) # 9 (up)
print(solution(66)) # 8 (up)

print(solution(1)) # 1 (down)
print(solution(2)) # 2 (down)
print(solution(3)) # 3 (down)
print(solution(4)) # 4 (down)
print(solution(5)) # 5 (down)
print(solution(6)) # 5 (up)
print(solution(7)) # 4 (up)
print(solution(8)) # 3 (up)
print(solution(9)) # 2 (up)
print(solution(10)) # 1 (up)


if __name__ == "__main__":
    from timeit import Timer
    query = [16, 2554, 2054, 44, 45, 46, 54, 55, 56, 455, 555, 64, 65, 66, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000000]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
