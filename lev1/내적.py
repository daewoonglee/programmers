def solution(a, b):
    return sum([n1*n2 for n1, n2 in zip(a, b)])


print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))

