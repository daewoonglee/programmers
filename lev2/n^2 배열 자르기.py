def solution(n, left, right):
    # 0.22997682099230587
    q, d = left // n, left % n
    ans = [q+1]*(q+1) + [i+1 for i in range(d+q+1,n)] if q > d else [i+1 for i in range(d, n)]
    for i in range(q+1, right//n+1):
        ans.extend([i+1]*i + [j+1 for j in range(i,n)])
    return ans[:right-left+1]


print(solution(3,2,5))
print(solution(4,7,14))


if __name__ == "__main__":
    from timeit import Timer
    query = [[4,7,14],[40,70,140],[400,4,14]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

