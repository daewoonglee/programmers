"""
문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.
예시
입력

5 3
출력

*****
*****
*****
"""
# 0:00:00.065125
n, m = map(int, input().strip().split(' '))
for _ in range(m):
    print("*" * n)

# code refactoring
# 0:00:00.027852
# n, m = map(int, input().strip().split(' '))
# print(("*" * n + "\n") * m)

from datetime import datetime
s = datetime.now()
for _ in range(100000):
    # for _ in range(m):
        # "*" * n
    ("*" * n + "\n") * m
print(datetime.now() - s)
