def solution(k, d):
    ans = 0
    for x in range(0, d + 1, k):
        # y = ((d ** 2 - x ** 2) ** 0.5) # 6.832716927
        y = ((d*d - x*x) ** 0.5) # 3.111694371
        # print(f"x: {x}, y: {y}, dist: {(x ** 2 + y ** 2) ** 0.5}")
        ans += y // k + 1
        """
        {(x*k)**2 + (y*k)**2}**0.5 <= d
        = {X + Y}**0.5 <= d*d**0.5 # X=(x*k)**2, Y=(y*k)**2
        = X+Y <= d*d
        = Y <= d*d-X
        = {(y*k)**2} <= d*d - (x*k)**2
        = {(y*k)**2}**0.5 <= {d*d - (x*k)**2}**0.5
        """
    return ans



print(solution(2, 4)) # 6
print(solution(1, 5)) # 26
print(solution(5, 9)) # 4


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [2, 4],
        [1, 5],
        [5, 9],
        [1, 1000000]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
