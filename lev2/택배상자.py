def solution(order):
    ans = 0
    stack = []
    box = 1
    order_idx = 0
    while order_idx < len(order):
        if box == order[order_idx]:
            ans += 1
            box += 1
            order_idx += 1
        elif stack and stack[-1] == order[order_idx]:
            ans += 1
            order_idx += 1
            stack.pop()
        elif stack and stack[-1] > order[order_idx]:
            break
        else:
            stack.append(box)
            box += 1
    return ans


print(solution([4,3,1,2,5])) # 2
print(solution([5,4,3,2,1])) # 5
