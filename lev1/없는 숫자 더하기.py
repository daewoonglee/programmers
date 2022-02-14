def solution(numbers):
    # 0.074751241132617
    #ans = 0
    #for n in range(10):
    #    if n not in numbers:
    #        ans += n
    #return ans

    # code refactoring - 0.02044590748846531
    return 45 - sum(numbers)


print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
print(solution([0]))
print(solution([0,1,2,3,4,5,6,7,8]))
print(solution([1,2,3,4,5,6,7,8,9]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[1,2,3,4,6,7,8,0], [5,8,4,0,6,7,9], [0], [0,1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8,9], [1], [2], [3]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

