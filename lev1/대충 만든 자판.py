def solution(keymap, targets):
    # # 0.727554059
    # key = {}
    # for km in keymap:
    #     for i, ch in enumerate(km):
    #         if ch not in key:
    #             key[ch] = i+1
    #         elif key[ch] > i+1:
    #             key[ch] = i+1
    #
    # ans = [0] * len(targets)
    # for i, target in enumerate(targets):
    #     for t in target:
    #         if t not in key:
    #             ans[i] = -1
    #             break
    #         ans[i] += key[t]
    # return ans

    # code refactoring - 0.880326636 (list indexing version)
    INF = 101 # 1~100까지 수만 문제에 나옴
    A = ord("A")
    key = [INF] * 26
    for km in keymap:
        for i, ch in enumerate(km):
            x = ord(ch) - A
            key[x] = i+1 if key[x] > i+1 else key[x]

    ans = [0] * len(targets)
    for i, target in enumerate(targets):
        for t in target:
            x = ord(t) - A
            if key[x] == INF:
                ans[i] = -1
                break
            ans[i] += key[x]
    return ans


# print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # [9,4]
# print(solution(["AA"], ["B"])) # [-1]
# print(solution(["AGZ", "BSSS"], ["ASA","BGZ"])) # [4,6]
print(solution(["A"], ["AA"])) # [2]
print(solution(["A"], ["AV"])) # [-1]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [["ABACD", "BCEFD"], ["ABCD","AABB"]],
        [["AA"], ["B"]],
        [["AGZ", "BSSS"], ["ASA","BGZ"]],
        [["A"], ["AA"]],
        [["A"], ["AV"]],
        [["A"]*100, ["A"]],
        [["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]*3, ["A"]*100],
        [["ABCDE"]*10, ["AB"]],
        [["ABCDE"]*10, ["ABCDE"]*10]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
