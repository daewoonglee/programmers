def solution(operations):
    ans = []
    for oper in operations:
        c, n = oper.split()
        # print(f"c: {c}, n: {n}, ans: {ans}")
        if c == "I":
            ans.append(int(n))
            ans.sort()
        elif ans:
            ans.pop() if n == "1" else ans.pop(0)
    return [ans[-1], ans[0]] if ans else [0, 0]


# print(solution(["I 16", "D 1"]))
# print(solution(["I 7", "I 5", "I -5", "D -1"]))
# print(solution(["I 7", "I 7", "I 7", "D -1", "D -1", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
