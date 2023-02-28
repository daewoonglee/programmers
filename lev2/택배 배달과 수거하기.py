def solution(cap, n, deliveries, pickups):
    def get_loc(delivery_list, pickup_list):
        d_idx, p_idx = n-1, n-1
        if delivery_list[-1] == 0 and pickup_list[-1] == 0:
            for i in range(n-1, -1, -1):
                if d_idx == n-1 and delivery_list[i] != 0:
                    d_idx = i
                if p_idx == n-1 and pickup_list[i] != 0:
                    p_idx = i

            if d_idx == n-1 and p_idx == n-1:
                return -1, -1
            elif d_idx == n-1:
                d_idx = p_idx
            elif p_idx == n-1:
                p_idx = d_idx
        return d_idx, p_idx

    def delivery_and_pickup(quota_list, idx, total=0):
        while idx >= 0:
            if quota_list[idx] != 0:
                diff = cap - (total + quota_list[idx])
                if diff == 0:
                    total = 0
                    quota_list[idx] = 0
                    while idx >= 0:
                        idx -= 1
                        if quota_list[idx] != 0:
                            break
                    break
                elif diff > 0:
                    total += quota_list[idx]
                    quota_list[idx] = 0
                else:
                    total = 0
                    quota_list[idx] = -diff
                    break
            idx -= 1
        return quota_list, idx, total

    ans = 0
    delivery_total, pickup_total = 0, 0
    delivery_idx, pickup_idx = get_loc(deliveries, pickups)
    while delivery_idx >= 0 or pickup_idx >= 0:
        ans += (max(delivery_idx, pickup_idx)+1) * 2
        deliveries, delivery_idx, delivery_total = delivery_and_pickup(deliveries, delivery_idx, delivery_total)
        pickups, pickup_idx, pickup_total = delivery_and_pickup(pickups, pickup_idx, pickup_total)
    return ans


"""
deliveries는 N만큼만 진행
진행하면서 최대 cap에 담을 수 있는 만큼만 전진하며 이동거리 더함
pickups는 위 deliveries에서 전진한 거리내에서 가장 멀리 있는 pickups들부터 없앰
deliveries N만큼 모두 진행한 뒤에 남은 pickups의 거리 계산하여 이동거리에 더함
"""

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])) # 16
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])) # 30
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 4, 0, 1, 0, 2, 0])) # 34
# print(solution(3, 7, [1, 1, 2, 0, 1, 1, 1], [3, 2, 2, 0, 0, 2, 0])) # 22
# print(solution(3, 7, [1, 1, 2, 0, 1, 1, 1], [0, 0, 2, 0, 2, 2, 3])) # 36
# print(solution(1, 1, [1], [1])) # 2
# print(solution(2, 2, [0, 1], [0, 1])) # 4
# print(solution(2, 2, [1, 0], [1, 0])) # 2
print(solution(2, 2, [0, 0], [0, 0])) # 0
