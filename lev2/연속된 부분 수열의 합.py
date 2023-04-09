def solution(sequence, k):
    ans = []
    N = len(sequence)
    i = 0
    j = 1
    total = sequence[0]
    while i < N:
        print(f"i: {i}, j: {j}, sum: {total}")
        if total < k and j < N:
            total += sequence[j]
            j += 1
        else:
            if total == k:
                ans.append([j-i, [i, j-1]])
            total -= sequence[i]
            i += 1
            if i >= j and j < N:
                if total == k:
                    ans.append([j-i, [i, j-1]])
            #     print(f"jj: {j}")
                total += sequence[j]
                j += 1
    ans.sort(key=lambda x: (x[0], x[1][0]))
    print(ans)
    return ans[0][1]

"""
max k에 해당하는 가장 짧은 구간 구하기

1. k에 해당하는 모든 구간 탐색
    1-1. sum(i ~ j) < k라면 -> j += 1
    1-2. sum(i ~ j) > k라면 -> i -= 1
    1-3. sum(i ~ j) == k라면 -> append ans 
2. 1번에서 구한 모든 구간 중 길이가 가장 짧은 경우 반환
    2-1 return min len <- ans 
"""


# print(solution([1, 2, 3, 4, 5], 7)) #[2, 3]
# print(solution([1, 1, 1, 2, 3, 4, 5], 5)) #[6, 6]
# print(solution([2, 2, 2, 2, 2], 6)) #[0, 2]
# print(solution([1,5,2,3,4,5,1,2,3,4,5], 6)) #[0 ,1]
# print(solution([5,4,3,2,1,2,3,4,5], 6)) #[2,4]
print(solution([7,8,9,10,1,2,3,4,5], 6)) #[4,6]
