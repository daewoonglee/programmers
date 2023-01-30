def solution(x, y, n):
    def conv_digit(x1, depth):
        if x1 == y:
            return depth
        elif x1 > y:
            return -1

        for num in sorted([conv_digit(x1+n, depth+1), conv_digit(x1*2, depth+1), conv_digit(x1*3, depth+1)]):
            if num != -1:
                return num
        return -1

    return conv_digit(x, 0)

"""
+n
*2
*3
"""

# print(solution(10, 40, 5)) # 2
# print(solution(9, 40, 1)) # 3
# print(solution(10, 40, 30)) # 1
# print(solution(2, 5, 4)) # -1
print(solution(1, 1000000, 1)) #
