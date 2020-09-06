"""
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
"""


def solution(arr1, arr2):
    # 0:00:01.047603
    return [[v1 + v2 for v1, v2 in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]

    # for speed
    # 0:00:00.900992
    # for i in range(len(arr1)):
    #     for j in range(len(arr1[i])):
    #         arr1[i][j] += arr1[i][j]
    # return arr1


# print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
# print(solution([[1, 2], [2, 3], [3, 4]], [[3, 4], [5, 6], [6, 7]]))
# print(solution([[1], [2]], [[3], [4]]))
# print(solution([[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]))


from datetime import datetime

s = datetime.now()
for _ in range(100000):
    solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])
    solution([[1, 2], [2, 3], [3, 4]], [[3, 4], [5, 6], [6, 7]])
    solution([[1], [2]], [[3], [4]])
    solution([[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]])
print(datetime.now() - s)
