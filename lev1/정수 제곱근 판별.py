"""
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.

입출력 예
n	return
121	144
3	-1

입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
"""

import math

def solution(n):
    # 0:00:00.151778
    # frac, whole = math.modf(n**0.5)
    # return -1 if frac else int(whole+1) ** 2

    # code refactoring
    # 0:00:00.098621
    # sqrt = n ** 0.5
    # return -1 if sqrt % 1 else int((sqrt + 1) ** 2)

    # 0: 00:00.105935
    sqrt = n ** 0.5
    return int((sqrt + 1) ** 2) if sqrt.is_integer() else -1


print(solution(121))
print(solution(3))
print(solution(144))

from datetime import datetime
s = datetime.now()
for _ in range(100000):
    solution(50000000000000)
    solution(343140123)
    solution(0)
print(datetime.now() - s)
