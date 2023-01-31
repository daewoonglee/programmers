def solution(numbers):
    # # 0.417511941
    # N = len(numbers)
    # ans = [-1] * N
    # idxs = [[0, numbers[0]]]
    # for i in range(1, N):
    #     while idxs and idxs[-1][1] < numbers[i]:
    #         ans[idxs.pop()[0]] = numbers[i]
    #     idxs.append([i, numbers[i]])
    # return ans

    # code refactoring - 0.40160762199999994
    ans = [-1] * len(numbers)
    idxs = [[-1, int(1e6)]]
    for i, num in enumerate(numbers):
        while idxs[-1][1] < num:
            ans[idxs.pop()[0]] = num
        idxs.append([i, num])
    return ans


# print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
# print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]
# print(solution([9, 1, 5, 4, 3, 2, 1, 6, 2])) # [-1, 5, 6, 6, 6, 6, 6, -1, -1]
print(solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 10])) # [2,3,10,2,3,10,2,3,10,-1]
print(solution([1, 2, 3, 1, 1, 2, 4, 2, 3, 10])) # [2,3,4,2,2,4,10,3,10,-1]
# print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1])) # [-1,-1,-1,-1,-1,-1,-1,-1,-1]
# print(solution([1, 2, 3, 4])) # [2,3,4,-1]
# print(solution([4, 3, 2, 1])) # [-1,-1,-1,-1]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [2, 3, 3, 5],
        [9, 1, 5, 3, 6, 2],
        [9, 1, 5, 4, 3, 2, 1, 6, 2],
        [1, 2, 3, 1, 2, 3, 1, 2, 3, 10],
        [1, 2, 3, 1, 1, 2, 4, 2, 3, 10],
        [1] * 10000,
        [i for i in range(1, 10001)]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=100))
