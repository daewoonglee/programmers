def solution(n, l, r):
    # bit = "11011"
    # for _ in range(n - 1):
    #     bit = bit * 2 + "0" * len(bit) + bit * 2
    # return bit[l - 1: r].count("1")

    def get_bit(N, d, t):
        total = 0
        while N > 2:
            N -= 1
            b = 4**N // 4
            LEN = 5**(N-1)
            q, d = divmod(d, LEN)

            if t == 'r':
                total += b * len([i for i in range(0, q) if i != 2])
            else:
                total += b * len([i for i in range(q+1, 5) if i != 2])

            print(f"whille loop n: {N}, bit: {b}, len: {LEN}, {t}q: {q}, {t}d: {d}, total{t}: {total}")

        if t == 'l':
            print(f"new {t}: {cantor[ld-1:].count('1')}, totalL: {total + cantor[ld-1:].count('1')}")
        else:
            print(f"new {t}: {4 - cantor[rd:].count('1')}, totalR: {total + 4 - cantor[rd:].count('1')}")
        return total + cantor[d-1:].count('1') if t == "l" else total + 4 - cantor[d:].count('1')

    cantor = "11011"
    if n == 1: return cantor[l-1:r].count("1")

    bit = 4**n // 4
    length = 5**(n-1)

    print(f"n: {n}, bit: {bit}, len: {length}")
    lq, ld = divmod(l, length)
    if lq > 0 and l % 5 == 0: lq -= 1
    rq, rd = divmod(r, length)
    print(f"l: {l, lq, ld}, lcan: {cantor[ld:]} r: {r, rq, rd}, rcan: {cantor[:rd+1]}")

    ans = bit * len([i for i in range(lq+1, rq) if i != 2])

    totalL = get_bit(n, ld, 'l') if lq != 2 else 0
    totalR = get_bit(n, rd, 'r') if rq != 2 else 0

    print(f"ans: {ans}, L: {totalL}, R: {totalR}")

    return ans + totalL + totalR

"""
1 2 3 4 5  6 7 8 9 10   11 12 13 14 15   16 17 18 19 20   21 22 23 24 25 (1-base)
1 1 0 1 1  1 1 0 1  1    0  0  0  0  0    1  1  0  1  1    1  1  0  1  1

n   bit                 total   len
1   1/1/0/1/1           4       5
2   4/4/0/4/4           16      25
3   16/16/0/16/16       64      125
4   64/64/0/64/64       256     625
5   256/256/0/256/256   1024    3125
"""


# print(solution(1, 2, 5)) # 3

# print(solution(2, 4, 8)) # 4
# print(solution(2, 4, 20)) # 10
# print(solution(2, 4, 25)) # 14
# print(solution(2, 4, 19)) # 9
# print(solution(2, 3, 14)) # 6
# print(solution(2, 17, 24)) # 6
# print(solution(2, 10, 24)) # 8

# print(solution(3, 4, 99)) # 45
# print(solution(3, 4, 100)) # 46
print(solution(3, 20, 25)) # 5
# print(solution(4, 4, 600)) # 238
# print(solution(4, 500, 600)) # 49
# print(solution(5, 1, 256)) # 128
# print(solution(20, 4, 19)) # 9
