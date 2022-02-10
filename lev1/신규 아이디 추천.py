import re
def solution(new_id):
    r1 = re.sub(r"[^a-zA-Z0-9._-]", "", new_id.lower())
    r2 = re.sub(r"(^\.+)|(\.+$)", "", r1)
    r3 = re.sub(r"(\.+){2,}", ".", r2)
    if not r3:
        return "aaa"
    elif len(r3) > 15:
        return r3[:15] if r3[14] != "." else r3[:14]
    elif len(r3) <= 2:
        return r3 + r3[-1]*(3-len(r3))
    else:
        return r3


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("1"))
print(solution("@"))

