"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	return
17	    3
011	    2

입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""


from itertools import permutations


def isprime(n):
    flag = False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = True
            break
    return True if not flag else False


def solution(numbers):
    # 0.11298603025000001
    # p_list = list(set(int(''.join(p)) for i in range(1, len(numbers)+1) for p in permutations(numbers, i)))
    # p_list = [p for p in p_list if p > 1]
    # return len([p for p in p_list if isprime(p)])

    # code refactoring
    # 0.11550581325000002
    p_set = set(int(''.join(p)) for i in range(1, len(numbers)+1) for p in permutations(numbers, i))
    p_set -= set(range(0, 2))
    return len([p for p in p_set if isprime(p)])


print(solution('11'))
print(solution('17'))
print(solution('011'))
print(solution('4444'))


import timeit
tests = ['11',
         '17',
         '011',
         '4444']
avg = 0.
for t in tests:
    avg += timeit.timeit(lambda: solution(t), number=10000)
print(avg / len(tests))
