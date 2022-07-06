def solution(A, B):
    A.sort()
    B.sort()
    ans = 0

    # 0.39583870299999996
    # ai, bi = 0, 0
    # N = len(B)
    # while bi < N:
    #     if A[ai] < B[bi]:
    #         ai += 1
    #         ans += 1
    #     bi += 1
    # return ans

    # code refactoring - 0.30750327099999997
    ai = 0
    for bi in range(len(B)):
        if A[ai] < B[bi]:
            ans += 1
            ai += 1
    return ans


# print(solution([5,1,3,7], [2,2,6,8]))
# print(solution([2,2,2,2], [1,1,1,1]))
print(solution([1,2,3,4,5], [2,2,3,4,5])) # 4


if __name__ == "__main__":
    from timeit import Timer
    query = [[[5,1,3,7], [2,2,6,8]],
             [[2,2,2,2], [1,1,1,1]],
             [[1,2,3,4,5], [2,2,3,4,5]],
             [[i for i in range(100)], [i for i in range(100)]],
             [[i for i in range(100)], [i for i in range(50)]*2]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
