def solution(stones, k):
    ans = max(stones)
    for i in range(len(stones)-k+1):
        m = max(stones[i:i+k])
        if ans > m:
            ans = m
    return ans


"""
1 <= stones len <= 200,000
1 <= stones[i] <= 200,000,000
1 <= k <= stones len

매번 루프 탐색으론 효율성이 안나올 가능성 높음
루프를 한번 탐색하며 k 값으로 건널 수 있는 중간 위치 값을 탐색, 가장 max 값을 반환하면 O(n)으로 돌 수 있음
    중간 위치 탐색은 stones에서 k 깂 슬라이스 구간 탐색
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
# print(solution([10],1)) # 10
# print(solution([5, 5, 5, 2, 2, 9], 3)) # 5

print(solution([5, 5, 6, 7, 7, 7], 3)) # 7
print(solution1([5, 5, 6, 7, 7, 7], 3)) # 6
