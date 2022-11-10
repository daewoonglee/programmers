def solution(babbling):
    pron = {
        "a": ["aya", 3],
        "y": ["ye", 2],
        "w": ["woo", 3],
        "m": ["ma", 2]
    }
    ans = 0
    for bbg in babbling:
        idx = 0
        check = ""
        while idx < len(bbg):
            ch = bbg[idx]
            if ch in pron and check != pron[ch][0] and bbg[idx: idx+pron[ch][1]] == pron[ch][0]:
                idx += pron[ch][1]
                check = pron[ch][0]
            else: break
        else: ans += 1
    return ans


# print(solution(["aya", "yee", "u", "maa"]))#1
# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))#2
print(solution(["aayaye", "uyeuuye", "yeye", "yemawoo", "ayaayaa", "mawooyeayama"]))#2
print(solution(["wooyemawooye"]))#1
