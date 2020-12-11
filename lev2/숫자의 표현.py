"""
문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.

예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

2 + 3 + 4 = 9
4 + 5 = 9
9 = 9

1 + 2 + 3 + 4 + 5 + 6 = 21
6 + 7 + 8 = 21
10 + 11 = 21
21 = 21

제한사항
n은 10,000 이하의 자연수 입니다.
입출력 예
n	result
15	4
입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.
"""


def solution(n):
    # 0.13668285060000002
    # answer = 1
    # for i in range(1, n//2+1):
    #     s = 0
    #     for j in range(i, n//2+2):
    #         s += j
    #         if s > n:
    #             break
    #         elif s == n:
    #             answer += 1
    #             break
    # return answer

    # code refactoring
    # 0.08512204279999999
    # answer = 1
    # for i in range(1, n//2+1):
    #     s = 0
    #     while s < n:
    #         s += i
    #         i += 1
    #     if s == n:
    #         answer += 1
    # return answer

    # 0.018500563000000005
    return len([i for i in range(1, n+1, 2) if n % i is 0])


print(solution(15))
print(solution(9))
print(solution(21))


import timeit
avg_time = 0.
tests = [15, 9, 21, 100, 99]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
