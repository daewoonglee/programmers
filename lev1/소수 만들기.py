from itertools import combinations
def solution(nums):
    ans = 0
    for c in combinations(nums, 3):
        total = sum(c)
        flag = False
        for n in range(2, int(total**0.5)+1):
            if total % n == 0:
                flag = True
                break
        if not flag:
            ans += 1
    return ans


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
print(solution([i for i in range(1, 51)]))

