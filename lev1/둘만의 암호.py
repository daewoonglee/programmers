def solution(s, skip, index):
    alpha = [ch for ch in "abcdefghijklmnopqrstuvwxyz"]
    for sk in skip:
        alpha.pop(alpha.index(sk))

    N = len(alpha)
    return "".join([alpha[(alpha.index(ch)+index) % N] for ch in s])


print(solution("aukks", "wbqd", 5)) # happy
