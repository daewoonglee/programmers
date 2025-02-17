def solution(n, w, num):
    h, d = n//w, n%w
    delivery = []
    box_num = 1
    for i in range(h):
        range_w = range(w) if i % 2 == 0 else range(w-1, -1, -1)
        delivery.append([box_num+j for j in range_w])
        box_num += w

    delivery.append(
        [box_num + j for j in range(d)] + [0] * (w - len(range(d))) if h % 2 == 0
        else [0] * (w - len(range(w - 1, w - d - 1, -1))) + [box_num + j for j in range(w - 1, w - d - 1, -1)]
    )
    print(delivery)

    start_i, start_j = 0, 0
    for i in range(h):
        for j in range(w):
            if delivery[i][j] == num:
                start_i, start_j = i, j
                break
    return h-start_i+1 if delivery[-1][start_j] else h-start_i


# print(solution(22, 6, 8)) # 3
# print(solution(13, 3, 6)) # 4
print(solution(13, 3, 7)) # 3
