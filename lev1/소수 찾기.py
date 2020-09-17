"""
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.

입출력 예
n	result
10	4
5	3

입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
"""

def solution(n):
    cnt = 0
    for i in range(2, n+1):
        flag = False
        if i % 2 == 0:
            cnt += 1 if i == 2 else 0
        else:
            # 1.1835615
            # for j in range(3, (i//2)+1):

            # 0.5282692333333333
            for j in range(3, int(i ** 0.5)+1):
                if i % j == 0:
                    flag = True
                    break
            if not flag:
                cnt += 1
    return cnt

    # if n % 2 == 0:
    #     return 'prime' if n == 2 else 'no prime'
    # else:
    #     flag = False
    #     for i in range(3, int(n ** 0.5)+1):
    #         if n % i == 0:
    #             flag = True
    #             break
    #     return 'prime' if not flag else 'no prime'

# print(f'2 pred: {solution(2)}')
# print(f'4 pred: {solution(4)}')
# print(f'10: {solution(10)}')
# print(f'5: {solution(5)}')
# print(f'80: {solution(80)}')
# print(f'1223: {solution(1223)}')

import timeit
avg_time = 0.
li = [2, 4, 10, 5, 80, 523]
for n in li:
    avg_time += timeit.timeit(lambda: solution(n), number=10000)
print(f'avg_time: {avg_time / len(li)}')
