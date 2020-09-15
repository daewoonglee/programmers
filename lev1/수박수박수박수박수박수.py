"""
문제 설명
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	수박수
4	수박수박
"""


def solution(n):
    # 0.007173800000000001
    return "수박" * (n//2) + "수" if n % 2 else "수박" * (n//2)


print(solution(4))
print(solution(3))
print(solution(300))

import timeit
avg_time = 0.
li = [300, 30000, 10, 100]
for n in li:
    avg_time += timeit.timeit(lambda: solution(n), number=10000)
print(f'avg_time: {avg_time / len(li)}')
