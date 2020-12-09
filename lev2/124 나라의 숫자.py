"""
문제 설명
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라
1	    1
2	    2
3	    4
4	    11
5	    12
6	    14
7	    21
8	    22
9	    24
10	    41
자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.

입출력 예
n	result
1	1
2	2
3	4
4	11
"""


def solution(n):
    # 0.031225314665789483
    # convert = {1: '1', 2: '2', 0: '4'}
    # e = 0
    # num = 0
    # while 1:
    #     num += 3**e
    #     if n < num:
    #         break
    #     e += 1
    #
    # answer = ''
    # cnt = 1
    # while 1:
    #     n, d = divmod(n, 3)
    #     if d == 0:
    #         n -= 1
    #     answer += convert[d]
    #     if n <= 1:
    #         if cnt < e:
    #             answer += '1'
    #         break
    #     cnt += 1
    # return answer[::-1]
    
    # code refactoring
    # 0.0134904039993368
    # num = ['1', '2', '4']
    # answer = ""
    # while n > 0:
    #     n -= 1
    #     answer = num[n % 3] + answer
    #     n //= 3
    # return answer

    # 0.019423008167602045
    # if n <= 3:
    #     return '124'[n - 1]
    # else:
    #     q, r = divmod(n - 1, 3)
    #     return solution(q) + '124'[r]

    # 0.0173225706651768
    return '' if n == 0 else solution((n - 1) // 3) + "412"[n % 3]


# print(solution(10))
# print(solution(33))
print(solution(24))


import timeit
avg_time = 0.
tests = [24, 10, 33, 1000, 10000, 500000]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
