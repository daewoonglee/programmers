def solution(stones, k):
    # 0.357573229
    left = 1
    right = max(stones)
    ans = 1
    while left <= right:
        cnt = 0
        mid = (right + left) // 2
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt == k:
                    ans = mid
                    right = mid - 1
                    break
            else:
                cnt = 0
        else:
            left = mid+1
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
print(solution([3, 3, 3, 2, 2, 9, 5, 5, 5, 4], 3)) # 3
# print(solution([2, 3, 6, 7, 8, 9, 10, 11, 12, 13], 3)) # 6


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[5, 4, 3, 2], 4],
        [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1],
        [[3, 4, 4, 4, 4, 4, 4, 4, 4, 4], 1],
        [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1],
        [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3],
        [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 3],
        [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 10],
        [[4, 4, 4, 4, 4, 4, 4, 1, 4, 4], 2],
        [[4, 4, 4, 4, 4, 4, 4, 2, 1, 4], 2],
        [[4, 3, 2, 1, 2, 3, 4, 1, 4, 1], 3],
        [[3, 1, 3, 4, 5, 3, 1, 3, 2, 5], 3],
        [[10], 1],
        [[5, 5, 5, 2, 2, 9], 3],
        [[5, 5, 6, 7, 7, 7], 3],
        [[5, 5, 5, 2, 2, 9, 3, 3, 3, 4], 3],
        [[3, 3, 3, 2, 2, 9, 5, 5, 5, 4], 3],
        [[2, 3, 6, 7, 8, 9, 10, 11, 12, 13], 3],
        [[i for i in range(1, 1000)], 1],
        [[i for i in range(1000, 1, -1)], 1]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
