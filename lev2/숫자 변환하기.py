def solution(x, y, n):
    # # 9.771994752
    # def conv_digit(nums, depth): # dfs -> bfs 수정
    #     res = set()
    #     for num in nums:
    #         if num == y: return depth
    #         res.add(num+n)
    #         res.add(num*2)
    #         res.add(num*3)
    #
    #     if all([1 if r > y else 0 for r in res]):
    #         return -1
    #     return conv_digit(res, depth+1)
    #
    # if x == y: return 0
    # return conv_digit([x+n, x*2, x*3], 1)

    # code refactoring - 0.6215587469999999, bottom up
    def conv_digit(nums, depth):
        li = list()
        for num in nums:
            if num == x: return depth

            if num % 2 == 0:
                li.append(num / 2)
            if num % 3 == 0:
                li.append(num / 3)
            li.append(num-n)

        if all([1 if r <= 0 else 0 for r in li]): return -1
        return conv_digit(li, depth+1)

    if x == y: return 0
    return conv_digit([y], 0)


# print(solution(10, 40, 5)) # 2
# print(solution(9, 40, 1)) # 3
# print(solution(10, 40, 30)) # 1
# print(solution(2, 5, 4)) # -1
print(solution(1, 1000000, 1)) # 19

if __name__ == "__main__":
    from timeit import Timer
    query = [
        [10, 40, 5],
        [9, 40, 1],
        [10, 40, 50],
        [2, 5, 4],
        [1, 1000000, 1],
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
