def solution(s):
    ans = 0
    brackets = {"[": "]", "(": ")", "{": "}"}
    for i in range(len(s)):
        stack = []
        flag = False
        for ch in s[i:]+s[:i]:
            if ch in brackets:
                stack.append(ch)
            else:
                if stack and brackets[stack[-1]] == ch:
                    stack.pop()
                else:
                    flag = True
                    break
        if not flag and not stack:
            ans += 1
    return ans


# print(solution("[](){}"))
# print(solution("}]()[{"))
# print(solution("[)(]"))
# print(solution("}"))
# print(solution("}}}{{{"))
# print(solution("((()))"))
print(solution("((())"))

