"""
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.

입출력 예
arr     	result
[2,6,8,14]	168
[1,2,3]	    6
"""
from math import gcd
from functools import reduce


def get_gcd(m, n):
    if m < n:
        t = n
        n = m
        m = t

    while 1:
        d = m % n
        if d == 0:
            break
        m = n
        n = d
    return n


def solution(arr):
    # 0.028602382000826765
    # for i in range(len(arr)-1):
    #     a, b = arr[i], arr[i+1]
    #     m = int(a * b / get_gcd(a, b))
    #     arr[i+1] = m
    # return arr[-1]

    # code refactoring
    # 0.01878237600249122
    # n = arr[0]
    # for a in arr[1:]:
    #     n = n * a // get_gcd(n, a)
    # return n

    # 0.015483738003240433
    # n = arr[0]
    # for a in arr[1:]:
    #     n = n * a // gcd(n, a)
    # return n

    # 0.018647045002580853
    return reduce(lambda a, b: a * b // gcd(a, b), arr)


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([2, 4]))
print(solution([20]))


import timeit
avg_time = 0.
tests = [[2, 6, 8, 14],
         [20],
         [100]]
# tests = [[2], [4], [10], [5], [80], [523]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(t)}')
