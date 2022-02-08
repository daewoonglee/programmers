def solution(s):
    word2num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    s = s.lower()
    N = len(s)
    idx = 0
    ans = ""
    while idx < N:
        if s[idx].isdigit():
            ans += s[idx]
            idx += 1
        else:
            for j in [3, 4, 5]:
                if s[idx:idx+j] in word2num:
                    ans += word2num[s[idx:idx+j]]
                    idx += j
                    break
    return int(ans)
    

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
print(solution("onetwothreefourfivesixseveneightnineone"))

