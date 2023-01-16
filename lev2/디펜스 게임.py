def solution(n, k, enemy):
    invincibility = sorted(enemy[:k])
    while n > 0 and k < len(enemy):
        if enemy[k] > invincibility[0]:
            n -= invincibility[0]
            invincibility[0] = enemy[k]
            invincibility.sort()
        else:
            n -= enemy[k]
        k += 1

    if k > len(enemy):
        return len(enemy)
    if n >= 0:
        return k
    else:
        return k-1


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(7, 3, [4, 2, 1, 3, 1, 4, 5, 3])) # 7
print(solution(7, 3, [4, 4, 4, 5, 2, 1, 1])) # 6
print(solution(7, 3, [2, 4, 3, 3, 5, 4, 3])) # 5
print(solution(7, 3, [4, 2, 3, 2, 5, 3, 6])) # 6
print(solution(2, 4, [3, 3, 3, 3])) # 4
print(solution(13, 5, [3, 3, 3, 3])) # 4
