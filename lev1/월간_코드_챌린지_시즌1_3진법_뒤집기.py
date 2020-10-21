'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
입출력 예
n	result
45	7
125	229
입출력 예 설명
입출력 예 #1

답을 도출하는 과정은 다음과 같습니다.
n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
45	1200	0021	7
따라서 7을 return 해야 합니다.
입출력 예 #2

답을 도출하는 과정은 다음과 같습니다.
n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
125	11122	22111	229
따라서 229를 return 해야 합니다.
'''


def ternary(n):
    return str(n) if n <= 2 else ternary(n // 3) + str(n % 3)

# 0.03749221133333334
# def solution(n):
#     return sum([int(t) * 3 ** i for i, t in enumerate(ternary(n))])

# code refactoring
# 0.027876804166666668, performance improvement 34%
def solution(n):
    answer = 0
    cnt = 1
    for i, b in enumerate(ternary(n)):
        answer += int(b) * cnt
        cnt *= 3
    return answer

print(solution(45))
print(solution(125))
print(solution(1))
print(solution(2))
print(solution(3))

import timeit
avg_time = 0.
tests = [45, 125, 1, 2, 3, 33333]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
