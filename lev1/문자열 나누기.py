def solution(s):
    ch = ""
    same, diff = 0, 0
    ans = 0
    flag = True
    for alpha in s:
        if flag:
            ch = alpha
            same += 1
            flag = False
        else:
            if alpha == ch:
                same += 1
            else:
                diff += 1
        if same == diff:
            ans += 1
            same, diff = 0, 0
            flag = True
    if same or diff: ans += 1
    return ans


print(solution("banana")) # 3
print(solution("abracadabra")) # 6
print(solution("aaabbaccccabba")) # 3
