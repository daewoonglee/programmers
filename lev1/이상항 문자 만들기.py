"""
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

입출력 예
s	return
try hello world	TrY HeLlO WoRlD
입출력 예 설명
try hello world는 세 단어 try, hello, world로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로,
홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다. 따라서 TrY HeLlO WoRlD 를 리턴합니다.
"""


def solution(s):
    # 0.0526592925
    # answer = ""
    # i = 0
    # for char in s:
    #     if ord(char) == 32:
    #         i = 1
    #     answer += char.lower() if i % 2 else char.upper()
    #     i += 1
    # return answer

    # code refactoring
    # 0.0439594665
    answer = ""
    i = 0
    for char in s:
        if char == ' ':
            i = 1
        answer += char.lower() if i % 2 else char.upper()
        i += 1
    return answer

    # 0.05031663199999999
    # answer = ""
    # s_list = s.split(' ')
    # for word in s_list:
    #     for i, char in enumerate(word):
    #         answer += char.lower() if i % 2 else char.upper()
    #     answer += ' '
    # return answer


print(solution("try hello world"))


import timeit
avg_time = 0.
for n in ["try hello world", "try hello world g abc"]:
    avg_time += timeit.timeit(lambda: solution(n), number=10000)
print(f'avg_time: {avg_time / 2}')