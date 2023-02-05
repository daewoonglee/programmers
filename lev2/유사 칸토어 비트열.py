def solution(n, l, r):
    cantor = {"1": "11011", "0": "00000"}
    bit = "1"
    for _ in range(n):
        bit = "".join([cantor[b] for b in bit])
    return bit[l-1: r].count("1")


print(solution(2, 4, 17)) # 8
