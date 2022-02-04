def solution(price, money, count):
    # 0.025914032012224197
    #total_price = 0
    #for c in range(count):
    #    total_price += (price * (c+1))
    #return total_price - money if total_price > money else 0

    # code refactoring - 0.007152557373046875
    #total_price = count * (2*price + (count-1)*price)/2
    #return total_price - money if total_price > money else 0 

    # code refactoring 01 - 0.008575525134801865 (callback function)
    return max(0, count*(2*price+(count-1)*price)/2)


print(solution(3, 20, 4))
print(solution(1, 200, 30))


if __name__ == "__main__":
    from timeit import Timer
    query = [[3, 20, 4], [1, 200, 30]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

