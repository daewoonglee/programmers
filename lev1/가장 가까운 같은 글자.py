def solution(s):
    ans = []
    log = dict()
    for i, ch in enumerate(s):
        ans.append(i-log[ch] if ch in log else -1)
        log[ch] = i
    return ans


print(solution("banana")) # [-1, -1, -1, 2, 2, 2]
print(solution("foobar")) # [-1, -1, 1, -1, -1, -1]
print(solution("aaaa")) # [-1, 1, 1, 1]
print(solution("abcd")) # [-1, -1, -1, -1]
print(solution("abcda")) # [-1, -1, -1, -1, 4]
