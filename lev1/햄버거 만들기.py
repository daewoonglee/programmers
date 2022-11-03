def solution(ingredient):
    ans = 0
    stack = []
    for igd in ingredient:
        stack.append(igd)
        # if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1: # 1.018187671
        if stack[-4:] == [1,2,3,1]: # 1.077183271
            [stack.pop() for _ in range(4)]
            ans += 1
    return ans


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
print(solution([1, 2, 1, 2, 3, 1, 2, 3, 3])) # 1
print(solution([1, 1, 2, 1, 2, 3, 3, 2, 3, 3])) # 0
print(solution([1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 2, 3, 3, 1, 2, 3, 3, 3, 3, 3])) # 0
print(solution([1, 2, 3] * 100)) # 50
print(solution([1, 1, 2, 1, 2, 1, 2, 3, 3, 3, 2, 3])) # 0
print(solution([1, 1, 1, 2, 3, 2, 3, 2, 3])) # 0
print(solution([3, 2, 1, 3, 2, 1, 3, 2, 3, 2, 3, 1])) # 0
print(solution([1,2,3,1,2,3,1,1,1,1,2,3,1,2,3,1])) # 3


if __name__ == "__main__":
    from timeit import Timer
    query = [[2, 1, 1, 2, 3, 1, 2, 3, 1],
             [1, 2, 1, 2, 3, 1, 2, 3, 3],
             [1, 1, 2, 1, 2, 3, 3, 2, 3, 3],
             [1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 2, 3, 3, 1, 2, 3, 3, 3, 3, 3],
             [1, 2, 3] * 100,
             [1, 1, 2, 1, 2, 1, 2, 3, 3, 3, 2, 3],
             [1, 1, 1, 2, 3, 2, 3, 2, 3],
             [3, 2, 1, 3, 2, 1, 3, 2, 3, 2, 3, 1],
             [1,2,3,1,2,3,1,1,1,1,2,3,1,2,3,1]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
