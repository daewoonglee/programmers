def solution(price, money, count):
    total_price = 0
    for c in range(count):
        total_price += (price * (c+1))
    return total_price - money if total_price > money else 0


print(solution(3, 20, 4))
print(solution(1, 200, 30))

