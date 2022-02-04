def solution(n):
    # 0.832480126991868
    #for i in range(2, n):
    #    if n % i == 1: return i
    #return n

    # code refactoring - 0.04768524132668972
    ans = n-1
    for i in range(2, int(n**0.5)+1):
        if ans % i == 0: return i
    return ans


print(solution(10))
print(solution(12))
print(solution(1001))
print(solution(1598))
print(solution(100002)) 


if __name__ == "__main__":
    from timeit import Timer
    query = [10, 12, 1001, 1598, 100002]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

