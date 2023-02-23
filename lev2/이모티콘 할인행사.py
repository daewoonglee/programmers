import math
from itertools import product


def solution(users, emoticons):
    ans = [0, 0]
    min_user_sale = math.ceil(min([sale for sale, _ in users]) / 10) * 10
    percentages = [i for i in range(min_user_sale, 50, 10)]

    for prod_percentages in list(product(percentages, repeat=len(emoticons))):
        # plus_service = 0
        # user_price = 0
        local_ans = [0, 0]
        for sale, max_price in users:
            local_user_price = 0
            for percentage, emoticon in zip(prod_percentages, emoticons):
                if sale <= percentage:
                    local_user_price += emoticon*(1-percentage/100)

            if local_user_price >= max_price:
                # plus_service += 1
                local_ans[0] += 1
            else:
                # user_price += local_user_price
                local_ans[1] += local_user_price

        # # 2.2728095250000004
        # if ans[0] < plus_service or (ans[0] == plus_service and ans[1] < user_price):
        #     ans = [plus_service, user_price]

        # code refactoring - 2.648288576
        # ans = max(ans, [plus_service, user_price])

        # code refactoring - 2.403000527
        if ans < local_ans:
            ans = local_ans

    return ans


# print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]
# print(solution([[40, 10000], [30, 10000], [25, 10000]], [7000, 9000])) # [2, 5400]
print(solution([[40, 10000], [35, 10400], [25, 10000]], [7000, 9000])) # [1, 10800]
# print(solution([[40, 2900], [11, 5200], [5, 5900], [40, 3100], [23, 10000], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])) # [4, 13860]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[[40, 10000], [25, 10000]], [7000, 9000]],
        [[[40, 10000], [30, 10000], [25, 10000]], [7000, 9000]],
        [[[40, 10000], [35, 10400], [25, 10000]], [7000, 9000]],
        [[[40, 2900], [11, 5200], [5, 5900], [40, 3100], [23, 10000], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]],
        [[[40, 29000], [10, 50000], [40, 40000], [30, 1000000], [20, 10000000], [30, 30000000], [20, 12345]], [10000, 1000000, 1000, 100, 1000000, 77777]],
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=100))
