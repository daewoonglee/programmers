"""
문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers,
타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

입출력 예
numbers	            target	    return
[1, 1, 1, 1, 1]	    3	        5
입출력 예 설명
문제에 나온 예와 같습니다.
"""

import itertools
def solution(numbers, target):
    # 0.367143979
    # cnt = 0
    # for p in itertools.product([-1, 1], repeat=len(numbers)):
    #     if target == sum([numbers[i] * n for i, n in enumerate(p)]):
    #         cnt += 1
    # return cnt

    # code refactoring
    # 0.07788101875
    # 나는 -1, 1에 대한 경우의 수를 구한 다음에 numbers를 방문하면서 -1, 1을 곱해줌
    
    # 따로 -1, 1를 곱할 필요없이 product하는 과정에서 -1, 1을 곱한 뒤 경우의 수둘울 구하도록 진행
    # 이후 map, sum을 이용하여 합계를 구
    l = [(x, -x) for x in numbers]
    s = list(map(sum, itertools.product(*l)))
    return s.count(target)


print(solution([1, 1, 1, 1, 1], 3))


import timeit
avg_time = 0.
tests = [[[1, 1, 1, 1, 1], 3],
         [[1, 1, 1, 1, 1], 2],
         [[1, 1, 1, 1, 1], 1],
         [[1, 1, 1, 1, 1, 1], 4]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(*t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')