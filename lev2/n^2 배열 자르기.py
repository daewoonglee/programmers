def solution(n, left, right):
    # 0.22567024896852672
    ans = []
    for i in range(left, right+1):
        q, d = i//n, i%n
        ans.append(max(q, d)+1)
    return ans


print(solution(3,2,5))
print(solution(4,7,14))


if __name__ == "__main__":
    from timeit import Timer
    query = [[4,7,14],[40,70,140],[400,4,14]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

