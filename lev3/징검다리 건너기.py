def solution(stones, k):
    temp = list()
    ans = float("inf")
    for i, stone in enumerate(stones):
        while temp and temp[-1][-1] < stone:
            temp.pop()
        temp.append([i, stone])
        if i >= k-1:
            if temp[0][0] <= i-k:
                temp.pop(0)
            if ans > temp[0][-1]:
                ans = temp[0][-1]
    return ans


# print(solution([5, 4, 3, 2], 4)) # 5
# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1)) # 1
# print(solution([3, 4, 4, 4, 4, 4, 4, 4, 4, 4], 1)) # 3
# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1)) # 1
# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3
# print(solution([4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 3)) # 4
# print(solution([4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 10)) # 4
# print(solution([4, 4, 4, 4, 4, 4, 4, 1, 4, 4], 2)) # 4
# print(solution([4, 4, 4, 4, 4, 4, 4, 2, 1, 4], 2)) # 2
# print(solution([4, 3, 2, 1, 2, 3, 4, 1, 4, 1], 3)) # 2
# print(solution([3, 1, 3, 4, 5, 3, 1, 3, 2, 5], 3)) # 3
# print(solution([10], 1)) # 10
# print(solution([5, 5, 5, 2, 2, 9], 3)) # 5
# print(solution([5, 5, 6, 7, 7, 7], 3)) # 6
print(solution([5, 5, 5, 2, 2, 9, 3, 3, 3, 4], 3)) # 3
print(solution([2, 3, 6, 7, 8, 9, 10, 11, 12, 13], 3)) # 6

