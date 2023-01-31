def solution(numbers):
    N = len(numbers)
    ans = [-1] * N
    idxs = [[0, numbers[0]]]
    for i in range(1, N):
        while idxs and idxs[-1][1] < numbers[i]:
            ans[idxs.pop()[0]] = numbers[i]
        idxs.append([i, numbers[i]])
    return ans


# print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
# print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]
# print(solution([9, 1, 5, 4, 3, 2, 1, 6, 2])) # [-1, 5, 6, 6, 6, 6, 6, -1, -1]
print(solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 10])) # [2,3,10,2,3,10,2,3,10,-1]
print(solution([1, 2, 3, 1, 1, 2, 4, 2, 3, 10])) # [2,3,4,2,2,4,10,3,10,-1]
# print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1])) # [-1,-1,-1,-1,-1,-1,-1,-1,-1]
# print(solution([1, 2, 3, 4])) # [2,3,4,-1]
# print(solution([4, 3, 2, 1])) # [-1,-1,-1,-1]
