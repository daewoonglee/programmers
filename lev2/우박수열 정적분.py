def solution(k, ranges):
    def collatz(n):
        li = [n]
        while n > 1:
            n = n//2 if n % 2 == 0 else n*3+1
            li.append(n)
        return li

    collatz_list = collatz(k)

    # # 0.553656661
    # N = len(collatz_list)
    # area = [(cl + collatz_list[i+1])/2 for i, cl in enumerate(collatz_list[:-1])]
    #
    # ans = []
    # for i in ranges:
    #     if i[0] == N+i[1]-1 < 0:
    #         ans.append(0.)
    #     elif i[0] > N+i[1]-1:
    #         ans.append(-1.)
    #     else:
    #         if i[1] == 0:
    #             ans.append(sum(area[i[0]:]))
    #         else:
    #             ans.append(sum(area[i[0]:i[1]]))
    # return ans

    # code refactoring - 0.453809352
    area = [(cl + collatz_list[i+1])/2 for i, cl in enumerate(collatz_list[:-1])]
    N = len(area)
    return [-1 if s > e+N else sum(area[s:e+N]) for s, e in ranges] # [2:2] -> [] -> 0


print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]])) # [33.0,31.5,0.0,-1.0]
print(solution(27, [[0,0],[0,-1],[2,-3],[3,-3],[100, 126]])) # [101426.0, 101424.5, 101299.5, 101217.0, 372.0]
print(solution(127, [[0,0],[0,-1],[2,-3],[3,-3],[0,46],[33,-1]])) # [28024.0, 28022.5, 27472.5, 27090.0, 28024.0, 229.0]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [5, [[0,0],[0,-1],[2,-3],[3,-3]]],
        [27, [[0,0],[0,-1],[2,-3],[3,-3],[100, 126]]],
        [127, [[0,0],[0,-1],[2,-3],[3,-3],[0,46],[33,-1]]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
