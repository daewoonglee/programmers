import math
from itertools import product


def solution(users, emoticons):
    ans = [0, 0]
    min_user_per = math.ceil(min([per for per, _ in users]) / 10) * 10
    percentages = [i for i in range(min_user_per, 50, 10)]
    print(min_user_per, percentages)
    print(f"product: {list(product(percentages, repeat=len(emoticons)))}")

    # 경우의 수를 어떻게 계산해야 하는가? 예로 이모티콘의 길이가 2개라면?
    for pers in list(product(percentages, repeat=len(emoticons))):
        plus_service = 0
        local_price = 0
        for user in users:
            local_user_price = 0
            for per, emoticon in zip(pers, emoticons):
                if user[0] <= per:
                    local_user_price += emoticon*(1-per/100)

            if local_user_price >= user[1]:
                plus_service += 1
            else:
                local_price += local_user_price

        if ans[0] < plus_service or (ans[0] == plus_service and ans[1] < local_price):
            ans = [plus_service, local_price]
            print(f"ans: {ans}, per: {pers}")

    return ans


"""
완탐, 이모티콘의 길이 최대 7개에 대한 할인율 4개의 경우의 수 4**7 * user길이
    경우의 수 줄이기
        users의 minimum 할인율보다 낮은 할인율의 경우는 고려하지 않아도 될 듯 
"""

# print(solution([[40, 10000], [25, 10000]], [7000, 9000])) # [1, 5400]
# print(solution([[40, 10000], [30, 10000], [25, 10000]], [7000, 9000])) # [2, 5400]
print(solution([[40, 10000], [35, 10400], [25, 10000]], [7000, 9000])) # [1, 10800]
# print(solution([[40, 2900], [11, 5200], [5, 5900], [40, 3100], [23, 10000], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])) # [4, 13860]

