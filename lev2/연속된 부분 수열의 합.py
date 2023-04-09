def solution(sequence, k):
    # # 0.244592551
    # ans = [[], float("inf")]
    # N = len(sequence)
    # i = 0
    # j = 1
    # total = sequence[0]
    # while i < N:
    #     if total < k and j < N:
    #         total += sequence[j]
    #         j += 1
    #     else:
    #         if total == k and j - i < ans[1]:
    #             ans = [[i, j - 1], j-i]
    #         total -= sequence[i]
    #         i += 1
    #         if i >= j and j < N:
    #             if total == k and j - i < ans[1]:
    #                 ans = [[i, j - 1], j-i]
    #             total += sequence[j]
    #             j += 1
    # return ans[0]

    # code refactoring - 0.21695578499999998
    ans = [[], float("inf")]
    N = len(sequence)
    j = 0
    total = 0
    for i in range(N):
        while total < k and j < N:
            total += sequence[j]
            j += 1
        if total == k and j - i < ans[1]:
            ans = [[i, j - 1], j-i]
        total -= sequence[i]
    return ans[0]


# print(solution([1, 2, 3, 4, 5], 7)) #[2, 3]
# print(solution([1, 1, 1, 2, 3, 4, 5], 5)) #[6, 6]
# print(solution([2, 2, 2, 2, 2], 6)) #[0, 2]
# print(solution([1,5,2,3,4,5,1,2,3,4,5], 6)) #[0 ,1]
# print(solution([5,4,3,2,1,2,3,4,5], 6)) #[2,4]
print(solution([7,8,9,10,1,2,3,4,5], 6)) #[4,6]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[1, 2, 3, 4, 5], 7],
        [[1, 1, 1, 2, 3, 4, 5], 5],
        [[2, 2, 2, 2, 2], 6],
        [[1,5,2,3,4,5,1,2,3,4,5], 6],
        [[5,4,3,2,1,2,3,4,5], 6],
        [[7,8,9,10,1,2,3,4,5], 6],
        [[1,2,3,4,1,5,6,1,7,8,9,10,9,8,7,6,1,5,1,4,1,3,2,1,1,1,1,1,1,1],5]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
