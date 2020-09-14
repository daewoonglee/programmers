"""
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
입출력 예
n	return
12	28
5	6

입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
"""

def solution(n):
    # 0.40314791666666666
    # return sum([i for i in range(1, n) if n % i == 0]) + n

    # code refactoring
    # 약수 성질 이해
    # 0.2067881
    return sum([i for i in range(1, (n // 2) + 1) if n % i == 0]) + n


print(solution(0))
print(solution(5))
print(solution(12))
print(solution(36))
print(solution(199))

import timeit
avg_time = 0.
li = [0, 5, 12, 36, 999, 3000]
for n in li:
    avg_time += timeit.timeit(lambda: solution(n), number=10000)
print(f'avg_time: {avg_time / len(li)}')
