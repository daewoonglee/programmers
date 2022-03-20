def solution(n, left, right):
    arr = [[0]*n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(i+1):
            arr[i][j] = num
            arr[j][i] = num
        num += 1
    return sum(arr, [])[left: right+1]


print(solution(3,2,5))
print(solution(4,7,14))

