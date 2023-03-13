from collections import deque


def solution(stones, k):
    temp = deque(stones[:k])
    max_value = max(temp)
    ans = max_value
    for i in range(k, len(stones)):
        val = temp.popleft()
        temp.append(stones[i])
        if val == max_value:
            max_value = max(temp)
            if ans > max_value:
                ans = max_value
    return ans


"""
루프를 한번 탐색하며 k 값 슬라이스하며 구간 탐색
탐색된 구간 내 maximum 값 < 이전 maximum 값이면 ans 재할당 
"""

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
print(solution([5, 5, 6, 7, 7, 7], 3)) # 6
print(solution([5, 5, 5, 2, 2, 9, 3, 3, 3, 4], 3)) # 3

