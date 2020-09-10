"""
문제 설명
정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.

입출력 예
num	return
3	Odd
4	Even
"""


def solution(num):
    # 0: 00:00.048994
    # return "Odd" if num % 2 else "Even"

    # code refactoring
    # 0:00:00.060079
    # % 최적화가 잘되어 있어서 비트연산이 더 느린 것으로 추측 (구현체 자체가 더 빨라서)
    return 'Odd' if num & 1 else 'Even'


print(solution(3))
print(solution(4))
print(solution(44))
print(solution(5))

from datetime import datetime
s = datetime.now()
for _ in range(100000):
    solution(3)
    solution(4)
    solution(44)
    solution(5)
print(datetime.now() - s)


