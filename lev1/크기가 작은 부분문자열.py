def solution(t, p):
    N = len(p)
    p = int(p)
    return sum([1 for i in range(len(t)-N+1) if int(t[i:i+N]) <= p])


# print(solution("3141592", "271")) # 2
# print(solution("500220839878", "7")) # 8
# print(solution("10203", "15")) # 3
print(solution("3000000", "9999")) # 4
print(solution("9999999", "3333")) # 0
