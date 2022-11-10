def solution(babbling):
    # # 1.194467851
    # pron = {
    #     "a": ["aya", 3],
    #     "y": ["ye", 2],
    #     "w": ["woo", 3],
    #     "m": ["ma", 2]
    # }
    # ans = 0
    # for bbg in babbling:
    #     idx = 0
    #     check = ""
    #     while idx < len(bbg):
    #         ch = bbg[idx]
    #         if ch in pron and check != pron[ch][0] and bbg[idx: idx+pron[ch][1]] == pron[ch][0]:
    #             idx += pron[ch][1]
    #             check = pron[ch][0]
    #         else: break
    #     else: ans += 1
    # return ans

    # code refactoring - 0.331881019
    ans = 0
    pron = ["aya", "ye", "woo", "ma"]
    for bbg in babbling:
        for p in pron:
            if p*2 in bbg: break
            bbg = bbg.replace(p, " ")
        if len(bbg.strip()) == 0: ans += 1
    return ans


# print(solution(["aya", "yee", "u", "maa"]))#1
# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))#2
# print(solution(["aayaye", "uyeuuye", "yeye", "yemawoo", "ayaayaa", "mawooyeayama"]))#2
print(solution(["wooyemawooye"]))#1


if __name__ == "__main__":
    from timeit import Timer
    query = [["aya", "yee", "u", "maa"],
             ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"],
             ["aayaye", "uyeuuye", "yeye", "yemawoo", "ayaayaa", "mawooyeayama"],
             ["wooyemawooye"],
             ["wooyemawooye"*30, "aya"*30, "yeayeyeayeyeayeyeayeyeayeyeayeyeayeyeayeye"]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
