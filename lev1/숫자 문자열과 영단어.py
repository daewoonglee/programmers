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
    ans = ""
    # 0.16021884605288506
    #idx = 0
    #while idx < N:
    #    if s[idx].isdigit():
    #        ans += s[idx]
    #        idx += 1
    #        for j in [3, 4, 5]:
    #            if s[idx:idx+j] in word2num:
    #                ans += word2num[s[idx:idx+j]]
    #                idx += j
    #                break
    #return int(ans)

    # code refactoring - 0.29748598858714104
    #start, end = 0, 1
    #while end <= N:
    #    if s[start:end].isdigit():
    #        ans += s[start:end]
    #        start += 1
    #    elif s[start:end] in word2num:
    #        ans += word2num[s[start:end]]
    #        start = end
    #    end += 1
    #return int(ans) 

    # code refactoring (R) - 0.0979218315333128
    for k, v in word2num.items():
        s = s.replace(k, v)
    return int(s)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("1234567891"))
print(solution("onetwothreefourfivesixseveneightnineone"))


if __name__ == "__main__":
    from timeit import Timer
    query = ["one4seveneight", "23four5six7", "2three45sixseven", "123", "onetwothreefourfivesixseveneightnineone"]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

