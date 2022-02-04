def solution(sizes):
    # 0.06123458221554756
    #for s in sizes:
    #    if s[0] < s[1]:
    #        t = s[0]
    #        s[0] = s[1]
    #        s[1] = t
    #    
    #max_w, max_h = sizes[0]
    #for s in sizes[1:]:
    #    if max_w < s[0]: max_w = s[0]
    #    if max_h < s[1]: max_h = s[1]
    #return max_w * max_h

    # code refactoring - 0.056851595640182495
    max_w, max_h = 0, 0
    for s in sizes:
        w, h = [s[0], s[1]] if s[0] > s[1] else [s[1], s[0]]
        if max_w < w: max_w = w
        if max_h < h: max_h = h
    return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
print(solution([[80, 10], [10, 50], [10, 60], [10, 70]]))
print(solution([[10, 70], [20, 60], [10, 50], [80, 10]]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[[60, 50], [30, 70], [60, 30], [80, 40]], [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]], [[80, 10], [10, 50], [10, 60], [10, 70]], [[10, 70], [20, 60], [10, 50], [80, 10]]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

