def solution(n, l, r):
    bit = "11011"
    for _ in range(n-1):
        bit = bit*2 + "0"*len(bit) + bit*2
    print(bit, len(bit))
    return bit[l-1: r].count("1")


print(solution(1, 4, 5)) # 8
print(solution(2, 4, 17)) # 8
print(solution(3, 4, 17)) # 8
print(solution(4, 4, 17)) # 8
print(solution(5, 4, 17)) # 8
# print(solution(20, 4, 17)) # 8
