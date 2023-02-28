def solution(cap, n, deliveries, pickups):
    def delivery_and_pickup(quota, idx, total=0):
        while idx >= 0:
            if quota[idx] != 0:
                diff = cap - (total + quota[idx])
                if diff == 0:
                    total = 0
                    quota[idx] = 0
                    while idx >= 0:
                        idx -= 1
                        if quota[idx] != 0:
                            break
                    break
                elif diff > 0:
                    total += quota[idx]
                    quota[idx] = 0
                else:
                    total = 0
                    quota[idx] = -diff
                    break
            idx -= 1
        return quota, idx, total

    ans = 0
    delivery_total, delivery_idx = 0, n-1
    pickup_total, pickup_idx = 0, n-1
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

cap 4
[1, 0, 3, 1, 2] deliveries
[0, 3, 0, 4, 0] pickups
5 + 5 + 3 + 3 = 16

cap 2
[1, 0, 2, 0, 1, 0, 2] deliveries
[0, 2, 0, 1, 0, 2, 0] pickups
7 + 7 + 5 + 5 + 3 + 3 = 30 (back)
3 + 3 + 5 + 5 + 7 + 7 = 30

cap 2
[1, 0, 2, 0, 1, 0, 2] deliveries
[0, 4, 0, 1, 0, 2, 0] pickups
7 + 7 + 5 + 5 + 3 + 3 + 2 + 2 = 34

cap 3
[1, 1, 2, 0, 1, 1, 1] deliveries
[3, 2, 2, 0, 0, 2, 0] pickups
7 + 7 + 3 + 3 + 1 + 1 (back)
3 + 3 + 6 + 6 + 7 + 7

cap 3
[1, 1, 2, 0, 1, 1, 1] deliveries
[0, 0, 2, 0, 2, 2, 3] pickups
7 + 7 + 6 + 6 + 5 + 5 = 36
3 + 3 + 6 + 6 + 7 + 7 + 7 + 7
"""

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])) # 16
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])) # 30
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 4, 0, 1, 0, 2, 0])) # 34
# print(solution(3, 7, [1, 1, 2, 0, 1, 1, 1], [3, 2, 2, 0, 0, 2, 0])) # 22
print(solution(3, 7, [1, 1, 2, 0, 1, 1, 1], [0, 0, 2, 0, 2, 2, 3])) # 36
