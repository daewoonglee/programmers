"""
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

입출력 예
arr	return
[1,2,3,4]	2.5
[5,5]	5
"""

from functools import reduce
def solution(arr):
    # 0: 00:00.038541
    # return sum(arr) / len(arr)

    # 0:00:00.081646
    return reduce(lambda x, y: x+y, arr) / len(arr)

print(solution([1, 2, 3, 4]))

from datetime import datetime
s = datetime.now()
for _ in range(100000):
    solution([1, 2, 3, 4])
print(datetime.now() - s)
