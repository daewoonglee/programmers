"""
문제 설명
정수 n이 매개변수로 주어집니다.
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

examples.png

제한사항
n은 1 이상 1,000 이하입니다.
입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

문제 예시와 같습니다.
입출력 예 #3

문제 예시와 같습니다.
"""
from itertools import chain


def solution(n):
    # 0.03731264171428572
    # li = [0] * (n * (n+1) // 2)
    # first = {v: i*2 for i, v in enumerate(range(n, 0, -3))}
    # second = [i for i in range(n-1, 0, -3)]
    # third = {v: n-i for i, v in enumerate(range(n-2, 0, -3))}
    # first[n] = 0
    #
    # plus_n = 0
    # s_flag = False
    # value = 1
    # idx = 0
    # while n:
    #     if n in first:
    #         plus_n = first[n]
    #         s_flag = False
    #     elif n in second:
    #         plus_n = 1
    #         s_flag = True
    #     elif n in third:
    #         plus_n = -third[n]
    #         s_flag = False
    #
    #     for i in range(n):
    #         idx += plus_n
    #         plus_n = 1 if s_flag else plus_n + 1
    #         li[idx] = value
    #         value += 1
    #     n -= 1
    # return li

    # code refactoring
    # 0.025880859285714288
    # li = [0] * (n * (n + 1) // 2)
    # n_loop = ((n - 1) // 3) + 1
    # value = 1
    # init_idx = 0
    # for i in range(n_loop):
    #     idx = init_idx + i * 4
    #     init_idx = idx
    #     jump = i * 2
    #     for j in range(n - 3 * i):
    #         if j != 0:
    #             idx += jump
    #         li[idx] = value
    #         value += 1
    #         jump += 1
    #
    #     for _ in range((n - 1) - 3 * i):
    #         idx += 1
    #         li[idx] = value
    #         value += 1
    #
    #     for j in range((n - 2) - 3 * i):
    #         idx -= n - i - j
    #         li[idx] = value
    #         value += 1
    #
    # return li

    # 0.037097911857142854
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return list(chain(*board))


# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(6))
print(solution(7))


import timeit
avg_time = 0.
tests = [1, 2, 3, 4, 5, 6, 7]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
