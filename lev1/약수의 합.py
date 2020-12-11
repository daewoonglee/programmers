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
import math
import numpy as np
from collections import defaultdict


def solution(n):
    if n in [0, 1]:
        return n

    prime_dict = defaultdict(int)
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            prime_dict[i] += 1
        else:
            i += 1
    print(prime_dict)

    prime_keys = [*prime_dict.keys()]
    print(f'prime_keys: {prime_keys}')
    k = prime_keys.pop(0)
    row = [[math.pow(k, i) for i in range(prime_dict[k] + 1)]]
    print(f'row: {row}')
    while prime_keys:
        k = prime_keys.pop(0)
        col = [[math.pow(k, i)] for i in range(prime_dict[k]+1)]
        print(f'col: {col}')
        d = np.dot(col, row)
        print(f'd: {d}')
        row = d.reshape(1, d.shape[0] * d.shape[1])
        print(f'reshpae row: {row}')
    try:
        return d.sum()
    except:
        return sum(row[0])


print(solution(5))
print(solution(12))
# print(solution(36))
# print(solution(199))
