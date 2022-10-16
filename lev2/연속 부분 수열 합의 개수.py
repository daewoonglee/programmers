def solution(elements):
    N = len(elements)
    for i in range(N-1):
        elements.extend([elements[i*N+j] + elements[(i+j+1)%N] for j in range(N)])
    return len(set(elements))


print(solution([7,9,1,1,4])) # 18
print(solution([1,1,1])) # 3
print(solution([1,9,7,4])) # 13
