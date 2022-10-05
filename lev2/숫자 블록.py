def solution(begin, end):
    MAX = 10000000
    ans = []
    if begin == 1:
        ans.append(0)
        begin += 1

    # # 5.057135046
    # for num in range(begin, end+1):
    #     for n in range(2, int(num**0.5)+1):
    #         if num % n == 0 and num // n <= MAX:
    #             ans.append(num//n)
    #             break
    #     else: ans.append(1)

    # code refactoring - 4.952039344
    # k 변수에 값을 받은 뒤 ans에 추가 (마지막 for-else 구문 삭제)
    for num in range(begin, end+1):
        k = 1
        for n in range(2, int(num ** 0.5)+1):
            if num % n == 0 and num // n <= MAX:
                k = num // n
                break
        ans.append(k)

    return ans


print(solution(1, 10)) # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
print(solution(1000000000, 1000000000)) # 10000000
print(solution(1000000000-9, 1000000000)) # [1, 2004008, 1, 1, 2247191, 1, 444247, 1447178, 9009009, 10000000]


if __name__ == "__main__":
    from timeit import Timer
    query = [[1,10],[1000000000-1, 1000000000], [2,10001], [1000000000-9999, 1000000000]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1))
