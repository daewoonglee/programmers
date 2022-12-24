def solution(s):
    # # 0.017090471000000003
    # ch = ""
    # same, diff = 0, 0
    # ans = 0
    # flag = True
    # for alpha in s:
    #     if flag:
    #         ch = alpha
    #         same += 1
    #         flag = False
    #     else:
    #         if alpha == ch: same += 1
    #         else: diff += 1
    #     if same == diff:
    #         ans += 1
    #         same, diff = 0, 0
    #         flag = True
    # if same or diff: ans += 1
    # return ans

    # code refactoring - 0.012088555999999997
    ans = 0
    same = 0
    diff = 0
    for alpha in s:
        if same == diff:
            ans += 1
            ch = alpha
        if alpha == ch: same += 1
        else: diff += 1
    return ans


print(solution("banana")) # 3
print(solution("abracadabra")) # 6
print(solution("aaabbaccccabba")) # 3


if __name__ == "__main__":
    from timeit import Timer
    query = ["banana",
             "abracadabra",
             "aaabbaccccabba",
             "aaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccc"]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))
