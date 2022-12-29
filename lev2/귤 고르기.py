from collections import Counter


def solution(k, tangerine):
    ans = 0

    # # 0.265255571
    # values = sorted(Counter(tangerine).values(), reverse=True)

    # approach idea - 0.551333608
    values = [0 for _ in range(len(tangerine))]
    for i in range(len(tangerine)): values[tangerine[i]-1] += 1
    values.sort(reverse=True)

    for _, v in values:
        if k > 0:
            ans += 1
            k -= v
        else: break
    return ans


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1


if __name__ == "__main__":
    from timeit import Timer
    query = [[6, [1, 3, 2, 5, 4, 5, 2, 3]],
             [4, [1, 3, 2, 5, 4, 5, 2, 3]],
             [2, [1, 1, 1, 1, 2, 2, 2, 3]],
             [1000, [i for i in range(1, 1000)]],
             [1000, [i for i in range(1, 1000)]*2]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
