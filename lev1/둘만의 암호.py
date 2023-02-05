def solution(s, skip, index):
    # # 0.196148172
    # alpha = [ch for ch in "abcdefghijklmnopqrstuvwxyz"]
    # for sk in skip:
    #     alpha.pop(alpha.index(sk))

    # 0.198809811
    alpha = [ch for ch in "abcdefghijklmnopqrstuvwxyz" if ch not in skip]

    N = len(alpha)
    return "".join([alpha[(alpha.index(ch)+index) % N] for ch in s])


print(solution("aukks", "wbqd", 5)) # happy


if __name__ == "__main__":
    from timeit import Timer
    query = [
        ["aukks", "wbqd", 5],
        ["a"*50, "b", 20],
        ["abc"*20, "z", 20]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
