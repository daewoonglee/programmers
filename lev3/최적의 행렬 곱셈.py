def solution(matrix_sizes):
    N = len(matrix_sizes)
    DP = [[0]*N for _ in range(N)]
    for i in range(N-2, -1, -1):
        for j in range(i+1, N): # i:1, j:2, i:0, j:1, i:0, j:2
            print(f"i: {i}, j: {j}")
            calc = []
            for m in range(i, j):
                calc.append(DP[i][m] + DP[m+1][j] + (matrix_sizes[i][0] * matrix_sizes[m][1] * matrix_sizes[j][1]))
            DP[i][j] = min(calc)
    return DP[0][N-1]

"""
[5,3], [3,10], [10,6]
[5, 3, 10, 6]

((A,B),C) = (5*3*10) + (5*10*6)
(A, (B, C)) = (5*3*6) + (3*10*6)

        0(A)    1(B)    2(C)
0(A)    0       150     270
1(B)    0       0       180
2(C)    0       0       0

DP[s][e] = min(DP[s][m] + DP[m+1][e] + S[0] * M[1] * E[1], s <= m < e)
DP[1][2] = min(DP[1][1] + DP[2][2] + matrix_sizes[1][0] * matrix_sizes[1][1] * matrix_sizes[2][1] = 180)
DP[0][1] = min(DP[0][0] + DP[1][1] + matrix_sizes[0][0] * matrix_sizes[0][1] * matrix_sizes[1][1] = 150)
DP[0][2] = min(
    DP[0][0] + DP[1][2] + matrix_sizes[0][0] * matrix_sizes[0][1] * matrix_sizes[2][1] = 0 + 180 + (5 * 3 * 6) = 270,
    DP[0][1] + DP[2][2] + matrix_sizes[0][0] * matrix_sizes[1][1] * matrix_sizes[2][1]  = 150 + 0 + (5 * 10 * 6) = 450
)
"""

# print(solution([[5,3],[3,10],[10,6]])) # 270
print(solution([[5,3],[3,10],[6,3],[10,6]]))
