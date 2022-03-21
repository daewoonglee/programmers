def solution(n, left, right):
    # 0.48373288102447987
    arr = []
    q = right // n + 1
    for i in range(n):
        arr.extend([i+1]*i + [j+1 for j in range(i,n)])
        if i >= q: break
    return arr[left: right+1]


print(solution(3,2,5))
print(solution(4,7,14))


if __name__ == "__main__":
    from timeit import Timer
    query = [[4,7,14],[40,70,140],[400,4,14]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

