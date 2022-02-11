# 0.22819807566702366
#import re
#def solution(new_id):
#    r1 = re.sub(r"[^a-zA-Z0-9._-]", "", new_id.lower())
#    r2 = re.sub(r"(^\.+)|(\.+$)", "", r1)
#    r3 = re.sub(r"(\.+){2,}", ".", r2)
#    if not r3:
#        return "aaa"
#    elif len(r3) > 15:
#        return r3[:15] if r3[14] != "." else r3[:14]
#    elif len(r3) <= 2:
#        return r3 + r3[-1]*(3-len(r3))
#    else:
#        return r3

# 0.2994337808340788 - without regular expression version
def solution(new_id):
    step1 = new_id.lower()
    step2 = "".join([ch for ch in step1 if ch.isalnum() or ch in ["-", "_", "."]])

    #step3 = step2[0] if step2 else ""
    #for ch in step2[1:]:
    #    if step3[-1] != "." or ch != ".":
    #        step3 += ch    

    # code refactoring - 0.1948608234524727
    step3 = step2
    while ".." in step3:
        step3 = step3.replace("..", ".")

    if step3:
        step4 = step3[1:] if step3[0] == "." else step3
        if step4 and step4[-1] == ".":
            step4 = step4[:-1]
    else:
        step4 = ""

    if not step4:
        return "aaa"    
    elif len(step4) > 15:
        return step4[:15] if step4[14] != "." else step4[:14]
    elif len(step4) < 3:
        return step4 + step4[-1] * (3-len(step4))
    else: 
        return step4


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("1"))
print(solution("@"))


if __name__ == "__main__":
    from timeit import Timer
    query = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p", "1", "@", "@"*1000, "1"*1000]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))

