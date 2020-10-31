"""
문제 설명
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다.
1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |
로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.
위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

제한사항
행의 개수 N : 100,000 이하의 자연수
열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
점수 : 100 이하의 자연수
입출력 예
land	answer
[[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.
"""


def solution(land):
    max_land = [[] for _ in land]
    for i, row in enumerate(land):
        second_largest_n, largest_n = sorted(row)[-2:]
        largest_idx = row.index(largest_n)
        second_idx = row.index(second_largest_n)
        max_land[i].append((largest_n, largest_idx))
        max_land[i].append((second_largest_n, second_idx))

    answers = [0 for _ in range(2)]
    for i in range(2):
        pre_idx = max_land[0][i][1]
        answers[i] += max_land[0][i][0]
        for m in max_land[1:]:
            for j in range(2):
                if pre_idx != m[j][1]:
                    pre_idx = m[j][1]
                    answers[i] += m[j][0]
                    break
    return max(answers)


# print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
# print(solution([[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]]))
# print(solution([[1, 2, 3, 50], [1, 2, 3, 51], [1, 2, 3, 100]]))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))

# import timeit
# avg_time = 0.
# tests = [[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]],
#          [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
#          [[100, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]]
# for t in tests:
#     avg_time += timeit.timeit(lambda: solution(t), number=10000)
# print(f'avg_time: {avg_time / len(tests)}')
