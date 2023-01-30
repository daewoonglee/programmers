def solution(x, y, n):
    def conv_digit(nums, depth): # dfs -> bfs 수정
        res = set()
        for num in nums:
            if num == y: return depth
            res.add(num+n)
            res.add(num*2)
            res.add(num*3)

        if all([1 if r > y else 0 for r in res]):
            return -1
        return conv_digit(res, depth+1)

    if x == y: return 0
    return conv_digit([x+n, x*2, x*3], 1)


# print(solution(10, 40, 5)) # 2
# print(solution(9, 40, 1)) # 3
# print(solution(10, 40, 30)) # 1
# print(solution(2, 5, 4)) # -1
print(solution(1, 1000000, 1)) #
