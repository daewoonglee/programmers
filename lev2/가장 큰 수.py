"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
numbers	            return
[6, 10, 2]	        6210
[3, 30, 34, 5, 9]   9534330
"""


from functools import cmp_to_key
def solution(numbers):
    # 0.027267047699999998
    # numbers = sorted(list(map(str,  numbers)), key=lambda x: x*4, reverse=True)
    # return str(int(''.join(numbers)))

    # 0.0661853225
    n = list(map(str, numbers))
    n = sorted(n, key=cmp_to_key(lambda x, y: int(y+x) - int(x+y)))
    return str(int(''.join(n)))


# print(solution([6, 10, 2]))
# print(solution([6, 20, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([3, 5, 9, 98, 99]))
print(solution([3, 5, 99, 989, 997, 999, 9]))
# print(solution([3, 5, 9, 97, 98, 997, 978]))
# print(solution([9, 96, 978]))
# print(solution([9, 978, 96]))
# print(solution([96, 9, 97, 87, 99, 976, 977]))
# print(solution([9999, 99999999]))
print(solution([0, 0]))

import timeit
avg_time = 0.
tests = [[6, 10, 2],
         [6, 20, 2],
         [3, 30, 34, 5, 9],
         [3, 5, 9, 98, 99],
         [3, 5, 99, 989, 997, 999, 9],
         [3, 5, 9, 97, 98, 997, 978],
         [9, 96, 978],
         [9, 978, 96],
         [96, 9, 97, 87, 99, 976, 977],
         [9999, 99999999]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
