def solution(t, p):
    N = len(p)
    # # compare int version - 11.850301761999999
    # p = int(p)
    # return sum([1 for i in range(len(t)-N+1) if int(t[i:i+N]) <= p])

    # compare str version - 5.240226359
    return sum([1 for i in range(len(t) - N + 1) if t[i:i + N] <= p])


print(solution("3141592", "271")) # 2
print(solution("500220839878", "7")) # 8
print(solution("10203", "15")) # 3
print(solution("3000000", "9999")) # 4
print(solution("9999999", "3333")) # 0


if __name__ == "__main__":
    from timeit import Timer
    query = [["3141592", "271"],
             ["500220839878", "7"],
             ["10203", "15"],
             ["3000000", "9999"],
             ["9999999", "3333"],
             ["9"*10000, "3"*18],
             ["3"*10000, "9"*18],
             ["3"*10000, "9"*1],
             ["9"*10000, "3"*1]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
