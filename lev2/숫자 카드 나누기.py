def solution(arrayA, arrayB):
    def get_intersection(arr):
        divisor = []
        for a in arr:
            local_divisor = set()
            for i in range(2, int(a**0.5)+1):
                if a % i == 0:
                    local_divisor.add(i)
                    local_divisor.add(a//i)
            local_divisor.add(a)
            divisor.append(local_divisor)
            # print(f"a: {a}, div: {local_divisor}")
        # print(f"a_div: {a_divisor}")
        inter = divisor[0]
        for a in divisor[1:]:
            inter = inter.intersection(a)
        return sorted(inter)[::-1]

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
