def solution(n, cores):
    empty = [c-1 for c in cores]
    n -= len(cores)
    while n:
        for i, e in enumerate(empty):
            if e: empty[i] -= 1
            else:
                empty[i] = cores[i]-1
                n -= 1
                if n == 0: return i+1
    return len(cores)


""" 선입선출
    1   2   3   4
1   O   O   O
2   O       O
3   O
4   O   O   O
"""

print(solution(6, [1, 2, 3])) # 2
print(solution(9, [1, 2, 3, 1])) # 4

