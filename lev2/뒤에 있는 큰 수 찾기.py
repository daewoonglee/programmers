def solution(numbers):
    N = len(numbers)
    ans = []
    for i, n in enumerate(numbers):
        for j in range(i+1, N):
            if n < numbers[j]:
                ans.append(numbers[j])
                break
        else: ans.append(-1)
    return ans


print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]
print(solution([1, 2, 3, 4])) # [2,3,4,-1]
print(solution([4, 3, 2, 1])) # [-1,-1,-1,-1]
