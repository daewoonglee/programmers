def solution(arrayA, arrayB):
    # # code refactoring - 3.162247924999999
    # def get_intersection_num(arr):
    #     def get_gcd(n1, n2):
    #         while n2 > 0:
    #             n1, n2 = n2, n1 % n2
    #         return n1
    #
    #     gcd_n = arr[0] # min num
    #     for n in arr[1:]:
    #         gcd_n = get_gcd(gcd_n, n)
    #     return gcd_n
    #
    # def get_integer(gcd_n, arr):
    #     for a in arr:
    #         if a % gcd_n == 0:
    #             break
    #     else:
    #         return gcd_n
    #     return 0
    #
    # a_gcd = get_intersection_num(arrayA)
    # b_gcd = get_intersection_num(arrayB)
    #
    # a_integer = get_integer(a_gcd, arrayB)
    # b_integer = get_integer(b_gcd, arrayA)
    # return max(a_integer, b_integer)

    # code refactoring02 - 0.20781585599999985
    from math import gcd
    def get_num(arr1, arr2):
        gcd_n = arr1[0]
        for n in arr1:
            if (gcd_n := gcd(gcd_n, n)) == 1: # 0.20781585599999985 walrus operator
                return 0
            # # 0.20316877499999997
            # gcd_n = gcd(gcd_n, n)
            # if gcd_n == 1:
            #     return 0

        for n in range(gcd_n, 1, -1):
            if gcd_n % n == 0 and all(a % n for a in arr2):
                return n
        return 0

    return max(get_num(arrayB, arrayA), get_num(arrayA, arrayB))


print(solution([10, 17], [5, 20])) # 0
print(solution([10, 20], [5, 17])) # 10
print(solution([14, 35, 119], [18, 30, 102])) # 7
print(solution([14, 35, 119], [18, 14, 30, 102])) # 0
print(solution([14, 14, 35, 119], [18, 30, 102])) # 7


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[10, 17], [5, 20]],
        [[10, 20], [5, 17]],
        [[14, 35, 119], [18, 30, 102]],
        [[14, 35, 119], [18, 14, 30, 102]],
        [[14, 14, 35, 119], [18, 30, 102]],
        [[i for i in range(1, 1000001)], [i for i in range(1, 500001)]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
