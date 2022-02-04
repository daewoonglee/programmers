def solution(sizes):
    for s in sizes:
        if s[0] < s[1]:
            t = s[0]
            s[0] = s[1]
            s[1] = t
        
    max_w, max_h = sizes[0]
    for s in sizes[1:]:
        if max_w < s[0]: max_w = s[0]
        if max_h < s[1]: max_h = s[1]
    return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
print(solution([[80, 10], [10, 50], [10, 60], [10, 70]]))
print(solution([[10, 70], [20, 60], [10, 50], [80, 10]]))

