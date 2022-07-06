def solution(A, B):
    A.sort()
    B.sort()
    ans = 0
    ai, bi = 0, 0
    N = len(B)
    while bi < N:
        if A[ai] < B[bi]:
            ai += 1
            ans += 1
        bi += 1
    return ans


# print(solution([5,1,3,7], [2,2,6,8]))
# print(solution([2,2,2,2], [1,1,1,1]))
print(solution([1,2,3,4,5], [2,2,3,4,5])) # 4

"""
1 2 3 4 5
2 2 3 4 5
2 3 4 5 2

"""
