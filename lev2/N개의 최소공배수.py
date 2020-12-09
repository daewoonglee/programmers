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


def prime_list(n):
    if n <= 3:
        return [1, 2, 3]

    sieve = [1] * n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = 0
    return [i for i in range(2, n) if sieve[i]]


def factorization(n, p):
    divs = []
    i = 0

    if n in p:
        return [n]

    while 1:
        if n in p:
            divs.append(d)
            break
        else:
            d, m = divmod(n, p[i])
            if m == 0:
                divs.append(p[i])
                n = d
            else:
                i += 1
    return divs


from collections import Counter
def solution(arr):
    primes = prime_list(max(arr))
    print(f'primes: {primes}')
    fact_list = list()
    for a in arr:
        fact_list.append(factorization(a, primes))
    print(fact_list)
    answers = dict()
    for f in fact_list:
        for k, v in Counter(f).items():
            if k not in answers:
                answers[k] = v
            elif answers[k] <= v:
                answers[k] = v
    print(answers)
    answer = 1
    for k, v in answers.items():
        answer *= k**v
    return answer


# print(solution([2, 6, 8, 14]))
# print(solution([1, 2, 3]))
print(solution([2, 4]))


# import timeit
# avg_time = 0.
# # tests = [[2, 6, 8, 14],
# #          [20],
# #          [100]]
# tests = [[2], [4], [10], [5], [80], [523]]
# for t in tests:
#     avg_time += timeit.timeit(lambda: solution(t), number=10000)
# print(f'avg_time: {avg_time / len(t)}')
