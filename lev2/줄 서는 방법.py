import math


def solution(n, k):
    li = [i for i in range(1, n+1)]
    # code refactoring - # 0.363528173
    f = 1
    for num in li: f *= num
    ans = []
    while n:
        # f = math.factorial(n) # 0.366991436
        g = f // n
        q = (k-1) // g
        ans.append(li.pop(q))
        f //= n
        k %= g
        n -= 1

    return ans


print(solution(3, 1))
print(solution(3, 2))
print(solution(3, 3))
print(solution(3, 4))
print(solution(3, 5))
print(solution(4, 5))
print(solution(4, 10))


if __name__ == "__main__":
    from timeit import Timer
    query = [[3,1],[3,2],[3,3],[3,4],[3,5],[4,5],[4,10],[20,243290200817664000],[18,640237370572800]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
