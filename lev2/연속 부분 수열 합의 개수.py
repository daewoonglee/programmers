def solution(elements):
    # # 3.5665202459999996
    # N = len(elements)
    # for i in range(N-1):
    #     elements.extend([elements[i*N+j] + elements[(i+j+1)%N] for j in range(N)])
    # return len(set(elements))

    # # code refactoring01 - 3.502403492
    # N = len(elements)
    # ans = set(elements)
    # add = [e for e in elements]
    # for i in range(1,N):
    #     for j in range(N):
    #         add[j] += elements[(i+j)%N]
    #         ans.add(add[j])
    # return len(ans)

    # code refactoring02 - 2.166569657 (no need indexing)
    N = len(elements)
    res = set(elements)
    for i in range(N):
        element = elements[i]
        for j in range(i+1, i+N):
            element += elements[j % N]
            res.add(element)
    return len(res)


print(solution([7,9,1,1,4])) # 18
print(solution([1,1,1])) # 3
print(solution([1,9,7,4])) # 13


if __name__ == "__main__":
    from timeit import Timer
    query = [[1 for _ in range(1,101)], [i for i in range(1,101)]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=1000))
