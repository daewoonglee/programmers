from collections import deque


def solution(queue1, queue2):
    # # 0.5435191640000001
    # queue1 = deque(queue1)
    # queue2 = deque(queue2)
    # queue1_sum = sum(queue1)
    # queue2_sum = sum(queue2)
    #
    # LIMIT = len(queue1) * 3 - 3
    # ans = 0
    # while queue1_sum != queue2_sum:
    #     if queue1_sum < queue2_sum:
    #         num = queue2.popleft()
    #         queue1.append(num)
    #         queue1_sum += num
    #         queue2_sum -= num
    #     else:
    #         num = queue1.popleft()
    #         queue2.append(num)
    #         queue1_sum -= num
    #         queue2_sum += num
    #
    #     ans += 1
    #     if ans > LIMIT:
    #         return -1
    # return ans

    # code refactoring - 0.4289445590000003
    target = (sum(queue1) + sum(queue2)) // 2
    queue_sum = sum(queue1)
    queue_list = queue1 + queue2 + queue1
    N = len(queue1) * 3 - 3

    pre = 0
    cur = len(queue1)
    ans = 0
    while queue_sum != target:
        if queue_sum < target:
            if cur >= N:
                return -1
            queue_sum += queue_list[cur]
            cur += 1
        else:
            queue_sum -= queue_list[pre]
            pre += 1
        ans += 1
    return ans


# print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
# print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
# print(solution([1, 1], [1, 5])) # -1
# print(solution([1000000000], [1000000000])) # 0
print(solution([1, 2, 1, 2], [1, 2, 10, 1])) # 9
print(solution([1, 2, 1, 2, 1], [1, 2, 1, 13, 2])) # 12
print(solution([1, 10, 1, 2], [1, 2, 1, 2])) # 7


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[3, 2, 7, 2], [4, 6, 5, 1]],
        [[1, 2, 1, 2], [1, 10, 1, 2]],
        [[1, 1], [1, 5]],
        [[1000000000], [1000000000]],
        [[1, 2, 1, 2], [1, 2, 10, 1]],
        [[1, 2, 1, 2, 1], [1, 2, 1, 13, 2]],
        [[i for i in range(1, 300001)], [i for i in range(1, 200001)]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
