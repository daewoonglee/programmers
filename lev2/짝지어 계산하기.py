"""
문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때,
짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.

입출력 예
s	result
baabaa	1
cdcd	0

입출력 예 설명
입출력 예 #1
위의 예시와 같습니다.
입출력 예 #2
문자열이 남아있지만 짝지어 제거할 수 있는 문자열이 더 이상 존재하지 않기 때문에 0을 반환합니다.

※ 공지 - 2020년 6월 8일 테스트케이스가 추가되었습니다.
"""


def get_pair(s, start=[0], jump=1, end=0):
    # print(f"s: {s}, start: {start}, jump: {jump}, end: {end}")
    if end == -1 or (start[-1]+jump == end and s[start[-1]] == s[start[-1]+jump]):
        return 1
    elif start[-1]+jump >= end:
        return 0

    if s[start[-1]] == s[start[-1]+jump]:
        if len(start) == 1:
            return get_pair(s, [start[-1]+jump+1], 1, end)
        else:
            if start[-1]+jump+1 == end:
                return get_pair(s, start[:-1], start[-1]+jump+1, end)
            return get_pair(s, start[:-1]+[start[-1]+jump+1], 1, end)

    for i in range(start[-1]+jump, end):
        if s[i] == s[i+1]:
            if i > 1:
                return get_pair(s, start+list(range(start[-1]+jump, i)), jump+2, end)
            else:
                return get_pair(s, start[:-1]+[i-1], jump+2, end)
    return 0


def solution(s):
    return get_pair(s, [0], 1, len(s)-1)


# print(solution("baabaa"))       # 1
# print(solution("cdcd"))         # 0
# print(solution(""))             # 1
# print(solution("c"))            # 0
# print(solution("cc"))           # 1
# print(solution("ccc"))          # 0
# print(solution("baaaabaa"))     # 1
# print(solution("baaaaabaa"))    # 0
# print(solution("baaaaabaaaa"))  # 0
# print(solution("baaabaaab"))    # 0
# print(solution("bbbaabaaaa"))   # 1
# print(solution("bbbaabbaaaaa"))   # 0
# print(solution("babbaaab"))   # 1
print(solution("babbaaaabba"))   # 1


# import timeit
# avg_time = 0.
# tests = ["baabaa",
#          "cdcd",
#          "c",
#          "",
#          "cc",
#          "ccc"]
# for t in tests:
#     avg_time += timeit.timeit(lambda: solution(t), number=10000)
# print(f'avg_time: {avg_time / len(tests)}')
