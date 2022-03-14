def solution(s):
    # 0.9609454079763964
    #ans = 0
    #brackets = {"[": "]", "(": ")", "{": "}"}
    #for i in range(len(s)):
    #    stack = []
    #    flag = False
    #    for ch in s[i:]+s[:i]:
    #        if ch in brackets:
    #            stack.append(ch)
    #        else:
    #            if stack and brackets[stack[-1]] == ch:
    #                stack.pop()
    #            else:
    #                flag = True
    #                break
    #    if not flag and not stack:
    #        ans += 1
    #return ans

    # code refactoring - 0.45960016804747283
    ans = 0
    for i in range(len(s)):
        rot_s = s[i:] + s[:i]
        while True:
            if "()" in rot_s: rot_s = rot_s.replace("()", "")
            elif "{}" in rot_s: rot_s = rot_s.replace("{}", "")
            elif "[]" in rot_s: rot_s = rot_s.replace("[]", "")
            else: break
        if not rot_s:
            ans += 1
    return ans


# print(solution("[](){}"))
# print(solution("}]()[{"))
# print(solution("[)(]"))
# print(solution("}"))
# print(solution("}}}{{{"))
# print(solution("((()))"))
print(solution("((())"))


if __name__ == "__main__":
    from timeit import Timer
    query = ["[](){}", "}]()[{", "[)(]", "}", "}}}{{{", "((()))", "((())", "{}"*15, "}"*30]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

