def solution(numbers):
    ans = 0
    for n in range(10):
        if n not in numbers:
            ans += n
    return ans


print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
print(solution([0]))
print(solution([0,1,2,3,4,5,6,7,8]))
print(solution([1,2,3,4,5,6,7,8,9]))

