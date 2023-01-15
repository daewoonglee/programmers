def solution(storey):
    ans = 0
    rnd = 0
    storey = str(storey)[::-1]
    for i, n in enumerate(storey):
        q = (int(n) + rnd)
        if q >= 5: # up
            ans += 10-q
            rnd = 0 if q == 5 and (i+1 == len(storey) or int(storey[i+1]) < 5) else 1
        else: # down
            ans += q
            rnd = 0
        # print(f"q: {q}, rnd: {rnd}, ans: {ans}")
    return ans + rnd


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
