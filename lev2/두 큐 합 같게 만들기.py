from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    print(q1_sum, q2_sum)

    LIMIT = len(q1) + len(q1) * 2 - 3
    ans = 0
    while q1_sum != q2_sum:
        if q1_sum < q2_sum:
            num = q2.popleft()
            q1.append(num)
            q1_sum += num
            q2_sum -= num
        else:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        print(f"q1: {q1_sum}, {q1}, q2: {q2_sum}, {q2}")
        ans += 1
        if ans > LIMIT:
            return -1
    return ans


"""
q1 sum, q2 sum 계산
1. q1s, q2s 중 값이 큰 경우의 sum에서 pop하여 작은 sum에 더한 후 값 비교
위 반복 q1s == q2s: return 
"""

# print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
# print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
# print(solution([1, 1], [1, 5])) # -1
# print(solution([1000000000], [1000000000])) # 0
print(solution([1, 2, 1, 2], [1, 2, 10, 1])) # 9
print(solution([1, 2, 1, 2, 1], [1, 2, 1, 13, 2])) # 12
