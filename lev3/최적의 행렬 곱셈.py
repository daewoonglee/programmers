def solution(matrix_sizes):
    N = len(matrix_sizes)
    global_ans = 2**31-1
    for i in range(N-1):
        info = [0] * N
        ans = 0
        w, h = matrix_sizes[i]
        info[i] = 1

        while 1:
            j = 0 # [5,3], [3,6] 계산 필요
            while j < N:
                if not info[j]:
                    if h == matrix_sizes[j][0]:
                        ans += (w * h * matrix_sizes[j][1])
                        h = matrix_sizes[j][1]
                    info[j] = 1
                    break
                j += 1
            else: break
        if sum(info) == N and global_ans > ans: global_ans = ans

    return global_ans


"""
중복된 행렬 값이 있을 수 있는가?, 지문에 중복이 없다는 말은 없음
[5,3], [3,10], [10,6]
[5,10], [3,6]

[5,3], [3,10] -> 150
[5,10], [10,6] -> 300

[3,10], [10,6] -> 180
[5,3], [3,6] -> 90
"""

print(solution([[5,3],[3,10],[10,6]])) # 270
# print(solution([[5,3],[3,10],[6,3],[10,6]]))
