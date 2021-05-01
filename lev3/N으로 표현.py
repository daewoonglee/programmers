"""
문제 설명
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
입출력 예
N	number	return
5	12	4
2	11	3
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

출처: https://www.oi.edu.pl/old/php/show.php?ac=e181413&module=show&file=zadania/oi6/monocyfr
※ 공지 - 2020년 9월 3일 테스트케이스가 추가되었습니다.
"""


def solution(N, number):
    if N == number:
        return 1
    global_stack = [set([int(str(N)*(i+1))]) for i in range(8)]
    for i in range(1, 8):
        for j in range(i):
            print(f"before i: {i}, stack: {global_stack[i]}, j: {j}, stack: {global_stack[j]}")
            for n1 in global_stack[j]:
                for n2 in global_stack[i-j-1]:
                    print(f"n1: {n1}, n2: {n2}")
                    global_stack[i].add(n1 + n2)
                    global_stack[i].add(n1 - n2)
                    global_stack[i].add(n1 * n2)
                    if n2 != 0:
                        global_stack[i].add(n1 // n2)
            print(f"after i: {i}, stack: {global_stack[i]}, j: {j}, stack: {global_stack[j]}")
            if number in global_stack[i]:
                return i+1
    return -1


print(solution(5, 5))
# print(solution(5, 12))      # 4
# print(solution(4, 12))      # 3
# print(solution(3, 12))      # 3
# print(solution(3, 3))       # 1
# print(solution(2, 11))      # 3
# print(solution(2, 12))      # 4
# print(solution(1, 12))      # 3
# print(solution(5, 31168))   # -1
print(solution(5, 7))    # 4
