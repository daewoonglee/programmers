"""
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.

입출력 예
s	n	result
AB	1	BC
z	1	a
a B z	4	e F d
"""
def solution(s, n):
    # answer = ""
    # lower = "abcdefghijklmnopqrstuvwxyz"
    # upper = lower.upper()
    #
    # # 0.014753599999999997
    # for char in s:
    #     if ord(char) == ord(' '):
    #         answer += ' '
    #     elif ord(char) <= ord('Z'):
    #         idx = upper.index(char) + n
    #         answer += upper[idx % len(upper)]
    #     else:
    #         idx = lower.index(char) + n
    #         answer += lower[idx % len(lower)]
    # return answer

    # code refactoring
    # 0.012572400000000003
    answer = ""
    for char in s:
        if char.isupper():
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        elif char.islower():
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += ' '
    return answer


print(solution("Z", 1))
print(solution("a B z", 4))

import timeit
avg_time = 0.
li = [('AB', 1), ('Z', 1), ('a B z', 4),]
for n in li:
    avg_time += timeit.timeit(lambda: solution(*n), number=10000)
print(f'avg_time: {avg_time / len(li)}')

