def solution(keymap, targets):
    key = {}
    for km in keymap:
        for i, ch in enumerate(km):
            if ch not in key:
                key[ch] = i+1
            elif key[ch] > i+1:
                key[ch] = i+1

    ans = [0] * len(targets)
    for i, target in enumerate(targets):
        for t in target:
            if t not in key:
                ans[i] = -1
                break
            ans[i] += key[t]
    return ans




"""
문자 별 최소 인덱스 위치 저장 후 탐색
{
    "A": 1, "B": 1, "C": 2, "D": 5, "E": 3, "F": 4
}
"""

# print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # [9,4]
# print(solution(["AA"], ["B"])) # [-1]
# print(solution(["AGZ", "BSSS"], ["ASA","BGZ"])) # [4,6]
print(solution(["A"], ["AA"])) # [2]
print(solution(["A"], ["AV"])) # [-1]
