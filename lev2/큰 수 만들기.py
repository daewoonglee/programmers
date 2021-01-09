"""
큰 수 만들기
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예
number	    k	return
1924	    2	94
1231234	    3	3234
4177252841	4	775841
"""


def solution(number, k):
    # 0.028590478599999997
    # N = len(number)
    # idx = 0
    # answer = ''
    # for i in range(N-k):
    #     if idx == k+i:
    #         answer += number[idx:]
    #         break
    #
    #     slice_number = number[idx:k+1+i]
    #     loc = 0
    #     for j, n in enumerate(slice_number[1:]):
    #         if slice_number[loc] < n:
    #             loc = j+1
    #         if n == '9':
    #             break
    #     idx += loc+1
    #     answer += slice_number[loc]
    # return answer

    # code refactoring
    # 0.025054389200000006
    # stack = [number[0]]
    # for num in number[1:]:
    #     while len(stack) > 0 and stack[-1] < num and k > 0:
    #         k -= 1
    #         stack.pop()
    #     stack.append(num)
    # if k != 0:
    #     stack = stack[:-k]
    # return ''.join(stack)

    # 0.023845939999999996
    st = []
    for n in number:
        while st and k > 0 and st[-1] < n:
            st.pop()
            k -= 1
        st.append(n)
    return ''.join(st[:len(st) - k])


print(solution("1924", 2))          # 94
print(solution("1924", 1))          # 924
print(solution("1231234", 3))       # 3234
print(solution("4177252841", 4))    # 775841
print(solution("15214111", 4))      # 5411
print(solution("4172253841", 4))    # 753841
print(solution("10000000", 1))      # 1000000
print(solution("99999999", 1))      # 9999999


import timeit
avg_time = 0.
tests = [["1924", 2],
         ["1924", 1],
         ["1231234", 3],
         ["4177252841", 4],
         ["15214111", 4]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(*t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')

