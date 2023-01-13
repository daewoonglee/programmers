def solution(arrayA, arrayB):
    def get_intersection(arr):
        def check_is_intersection(num):
            for sa in sorted_arr[1:]:
                if sa % num != 0: return -1
            return num

        sorted_arr = sorted(arr)
        n = sorted_arr[0] # min num
        divisor = []
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                if check_is_intersection(i) != -1:
                    divisor.append(i)
                if check_is_intersection(n//i) != -1:
                    divisor.append(n//i)
        if check_is_intersection(n) != -1:
            divisor.append(n)
        return sorted(divisor)[::-1]

    def get_integer(inter_list, arr):
        integer = 0
        for n in inter_list:
            for a in arr:
                if a % n == 0:
                    break
            else:
                return n
        return integer

    a_inter = get_intersection(arrayA)
    b_inter = get_intersection(arrayB)

    a_integer = get_integer(a_inter, arrayB)
    b_integer = get_integer(b_inter, arrayA)
    return max(a_integer, b_integer)


print(solution([10, 17], [5, 20])) # 0
print(solution([10, 20], [5, 17])) # 10
print(solution([14, 35, 119], [18, 30, 102])) # 7
print(solution([14, 35, 119], [18, 14, 30, 102])) # 0
print(solution([14, 14, 35, 119], [18, 30, 102])) # 7
