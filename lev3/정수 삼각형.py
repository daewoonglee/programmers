"""
문제 설명
스크린샷 2018-09-14 오후 5.44.19.png

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.
예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle_temp이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
입출력 예
triangle_temp	                                                result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	    30
출처
"""


from copy import deepcopy
def solution(triangle):
    # 0.298445245
    # triangle_temp = deepcopy(triangle)
    # max_sum = triangle[0][0]
    # for i in range(1, len(triangle)):
    #     for j in range(i):
    #         if triangle[i][j] < triangle_temp[i][j] + triangle[i-1][j]:
    #             triangle[i][j] = triangle_temp[i][j] + triangle[i-1][j]
    #         if triangle[i][j+1] < triangle_temp[i][j+1] + triangle[i-1][j]:
    #             triangle[i][j+1] = triangle_temp[i][j+1] + triangle[i-1][j]
    #         if max_sum < triangle[i][j]:
    #             max_sum = triangle[i][j]
    #         if max_sum < triangle[i][j+1]:
    #             max_sum = triangle[i][j+1]
    # return max_sum

    # code refactoring 01 - 0.260138399
    # triangle_temp = deepcopy(triangle)
    # for i in range(1, len(triangle)):
    #     for j in range(i):
    #         if triangle[i][j] < triangle_temp[i][j] + triangle[i-1][j]:
    #             triangle[i][j] = triangle_temp[i][j] + triangle[i-1][j]
    #         if triangle[i][j+1] < triangle_temp[i][j+1] + triangle[i-1][j]:
    #             triangle[i][j+1] = triangle_temp[i][j+1] + triangle[i-1][j]
    # return max(triangle[-1])

    # code refactoring 02 - 0.075924312
    # for t in range(1, len(triangle)):
    #     for i in range(t+1):
    #         if i == 0:
    #             triangle[t][0] += triangle[t-1][0]
    #         elif i == t:
    #             triangle[t][-1] += triangle[t-1][-1]
    #         else:
    #             triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    # return max(triangle[-1])

    # code refactoring 03 - 0.086990964
    l = []
    for r in triangle:
        l = [max(t, y) + z for t, y, z in zip([0]+l, l+[0], r)]
    return max(l)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
# print(solution([[0]]))


if __name__ == '__main__':
    from timeit import Timer
    query = [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],
             [[0]]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
