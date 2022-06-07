def solution(n, cores):
    # ver1. 테스트 (14/14), 효율성 (0/6)
    # cycle_cores = [1 for _ in cores]
    # empty = [c-1 for c in cores]
    # len_cores = len(cores)
    # N = n
    # n -= len_cores
    # while n:
    #     for i, e in enumerate(empty):
    #         if e:
    #             empty[i] -= 1
    #             cycle_cores.append(0)
    #         else:
    #             empty[i] = cores[i]-1
    #             n -= 1
    #             cycle_cores.append(1)
    #             if n == 0: return i+1
    #     if sum(cycle_cores[-len_cores:]) == len_cores: break
    #
    # cnt = cycle_cores[:-len_cores].count(1)
    # m = N%cnt
    # idx = 0
    # for i, cc in enumerate(cycle_cores[:-len_cores]):
    #     if cc: idx += 1
    #     if idx == m: return i%len_cores+1
    # return len_cores

    # ver2. 테스트 (2/14, 런타임 에러), 효율성 (0/6)
    def gcd(a, b):
        while b != 0:
            a, b = b, a%b
        return a

    def lcd(a, b):
        return int(a*(b/gcd(a,b)))

    g = cores[0]
    for i in range(1, len(cores)-1):
        g = gcd(g, cores[i])

    mul = 1
    for c in cores:
        mul *= c

    l = lcd(mul, g)
    cycle = sum(l//c for c in cores)

    m = n%cycle
    if m <= len(cores): return m if m else len(cores)

    empty = [c-1 for c in cores]
    m -= len(cores)
    while m:
        for i, e in enumerate(empty):
            if e:
                empty[i] -= 1
            else:
                empty[i] = cores[i]-1
                m -= 1
                if m == 0: return i+1
    return len(cores)


""" 선입선출
    1   2   3   1
1   O   O   O   O   [1  1   1   1]  0   1   2   3
2   O           O   [1  0   0   1]  4   5   6   7
3   O   O       O   [1  1   0   1]  8   9   10  11
4   O       O   O   [1  0   1   1]  12  13  14  15
5   O   O       O   [1  1   0   1]  16  17  18  19
6   O           O   [1  0   0   1]  20  21  22  23
7   O   O   O   O   [1  1   1   1]  

1   2   3   4   5   6   7   8   9   10  11  12  13
1   O   O   O   O   O   O   O   O   O    O   O   O   O
2   O       O       O       O       O        O       O
3   O           O           O            O           O
4   O   O   O   O   O   O   O   O   O    O   O   O   O
"""

# print(solution(6, [1, 2, 3])) # 2
# print(solution(22, [1, 2, 3, 1])) # 1
print(solution(34, [1, 2, 3, 1])) # 4
print(solution(330, [1, 2, 3, 1])) # 1
print(solution(324, [1, 2])) # 2
print(solution(3, [1, 3])) # 1
