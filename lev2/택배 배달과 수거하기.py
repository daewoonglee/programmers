def solution(cap, n, deliveries, pickups):
    # # 2.069277969
    # def get_loc(delivery_list, pickup_list):
    #     d_idx, p_idx = n-1, n-1
    #     if delivery_list[-1] == 0 and pickup_list[-1] == 0:
    #         for i in range(n-1, -1, -1):
    #             if d_idx == n-1 and delivery_list[i] != 0:
    #                 d_idx = i
    #             if p_idx == n-1 and pickup_list[i] != 0:
    #                 p_idx = i
    #
    #         if d_idx == n-1 and p_idx == n-1:
    #             return -1, -1
    #         elif d_idx == n-1:
    #             d_idx = p_idx
    #         elif p_idx == n-1:
    #             p_idx = d_idx
    #     return d_idx, p_idx
    #
    # def delivery_and_pickup(quota_list, idx, total=0):
    #     while idx >= 0:
    #         if quota_list[idx] != 0:
    #             diff = cap - (total + quota_list[idx])
    #             if diff == 0:
    #                 total = 0
    #                 quota_list[idx] = 0
    #                 while idx >= 0:
    #                     idx -= 1
    #                     if quota_list[idx] != 0:
    #                         break
    #                 break
    #             elif diff > 0:
    #                 total += quota_list[idx]
    #                 quota_list[idx] = 0
    #             else:
    #                 total = 0
    #                 quota_list[idx] = -diff
    #                 break
    #         idx -= 1
    #     return quota_list, idx, total
    #
    # ans = 0
    # delivery_total, pickup_total = 0, 0
    # delivery_idx, pickup_idx = get_loc(deliveries, pickups)
    # while delivery_idx >= 0 or pickup_idx >= 0:
    #     ans += (max(delivery_idx, pickup_idx)+1) * 2
    #     deliveries, delivery_idx, delivery_total = delivery_and_pickup(deliveries, delivery_idx, delivery_total)
    #     pickups, pickup_idx, pickup_total = delivery_and_pickup(pickups, pickup_idx, pickup_total)
    # return ans

    # code refactoring - 0.39120130799999997
    def get_loc(delivery_list, pickup_list):
        d_idx, p_idx = n-1, n-1
        if delivery_list[-1] == 0 and pickup_list[-1] == 0:
            for i in range(n-1, -1, -1):
                if d_idx == n-1 and delivery_list[i] != 0:
                    d_idx = i
                if p_idx == n-1 and pickup_list[i] != 0:
                    p_idx = i

            if d_idx == n-1 and p_idx == n-1:
                return -1
        return max(d_idx, p_idx)

    ans = 0
    delivery_total = 0
    pickup_total = 0
    loc = get_loc(deliveries, pickups)
    for i in range(n-1, -1, -1):
        delivery_total += deliveries[i]
        pickup_total += pickups[i]
        while delivery_total > cap or pickup_total > cap:
            delivery_total -= cap
            pickup_total -= cap
            ans += 2 * (loc + 1)
            loc = i
    if delivery_total > 0 or pickup_total > 0:
        ans += 2 * (loc + 1)
    return ans


# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])) # 16
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])) # 30
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 4, 0, 1, 0, 2, 0])) # 34
# print(solution(3, 7, [1, 1, 2, 0, 1, 1, 1], [3, 2, 2, 0, 0, 2, 0])) # 22
# print(solution(3, 7, [1, 1, 2, 0, 1, 1, 1], [0, 0, 2, 0, 2, 2, 3])) # 36
# print(solution(1, 1, [1], [1])) # 2
# print(solution(2, 2, [0, 1], [0, 1])) # 4
print(solution(2, 2, [1, 0], [1, 0])) # 2
print(solution(2, 2, [0, 0], [0, 0])) # 0


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]],
        [2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]],
        [2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 4, 0, 1, 0, 2, 0]],
        [3, 7, [1, 1, 2, 0, 1, 1, 1], [3, 2, 2, 0, 0, 2, 0]],
        [3, 7, [1, 1, 2, 0, 1, 1, 1], [0, 0, 2, 0, 2, 2, 3]],
        [1, 1, [1], [1]],
        [2, 2, [0, 1], [0, 1]],
        [2, 2, [1, 0], [1, 0]],
        [2, 2, [0, 0], [0, 0]],
        [2, 1000, [0]*1000, [0]*1000],
        [2, 1000, [0]*999 + [1], [0]*1000],
        [2, 1000, [i for i in range(1000)], [i for i in range(1000)]]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
