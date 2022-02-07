def solution(a, b):
    # 0.2342683169990778
    #return sum([n1*n2 for n1, n2 in zip(a, b)])

    # 0.27750201895833015
    return sum(map(lambda n1, n2: n1*n2, a, b))


print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[[1,2,3,4], [-3,-1,0,2]], [[-1,0,1], [1,0,-1]], [[i for i in range(300)], [i for i in range(300)]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

