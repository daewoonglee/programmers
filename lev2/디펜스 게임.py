import heapq


def solution(n, k, enemy):
    # code refactoring - 1.4233556000000007
    invincibility = enemy[:k]
    heapq.heapify(invincibility)
    # idx는 0부터 시작해서 start=k
    for stage, stage_enemy in enumerate(enemy[k:], start=k):
        if stage_enemy > invincibility[0]:
            n -= heapq.heappop(invincibility)
            heapq.heappush(invincibility, stage_enemy)
        else:
            n -= stage_enemy

        if n < 0: return stage
    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(7, 3, [4, 2, 1, 3, 1, 4, 5, 3])) # 7
print(solution(7, 3, [4, 4, 4, 5, 2, 1, 1])) # 6
print(solution(7, 3, [2, 4, 3, 3, 5, 4, 3])) # 5
print(solution(7, 3, [4, 2, 3, 2, 5, 3, 6])) # 6
print(solution(2, 4, [3, 3, 3, 3])) # 4
print(solution(13, 5, [3, 3, 3, 3])) # 4



if __name__ == "__main__":
    from timeit import Timer
    query = [
        [7, 3, [4, 2, 4, 5, 3, 3, 1]],
        [7, 3, [4, 2, 1, 3, 1, 4, 5, 3]],
        [7, 3, [4, 4, 4, 5, 2, 1, 1]],
        [7, 3, [2, 4, 3, 3, 5, 4, 3]],
        [7, 3, [4, 2, 3, 2, 5, 3, 6]],
        [2, 4, [3, 3, 3, 3]],
        [13, 5, [3, 3, 3, 3]],
        [1000000000, 1, [1000]*1000000],
        [1, 500000, [1000000]*1000000],
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
