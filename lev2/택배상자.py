def solution(order):
    ans = 0
    stack = []
    box = 1
    order_idx = 0

    # # 7.292721571
    # while order_idx < len(order):
    #     if box == order[order_idx]:
    #         ans += 1
    #         box += 1
    #         order_idx += 1
    #     elif stack and stack[-1] == order[order_idx]:
    #         ans += 1
    #         order_idx += 1
    #         stack.pop()
    #     elif stack and stack[-1] > order[order_idx]:
    #         break
    #     else:
    #         stack.append(box)
    #         box += 1
    # return ans

    # code refactoring 01 - 5.912291327
    # for n in range(1, len(order)+1):
    #     stack.append(n)
    #     while stack[-1] == order[order_idx]:
    #         ans += 1
    #         order_idx += 1
    #         stack.pop()
    #         if not stack or stack[-1] > order[order_idx]: break
    # return ans

    # code refactoring 02 - 3.877951898000001
    for o in order:
        if o == box:
            ans += 1
            box = o
        elif o > box:
            ans += 1
            stack.extend(range(box, o))
            box = o
        elif stack and o == stack.pop():
            ans += 1
        else:
            break
    return ans


print(solution([4,3,1,2,5])) # 2
print(solution([5,4,3,2,1])) # 5


if __name__ == "__main__":
    from timeit import Timer
    query = [[4,3,1,2,5], [5,4,3,2,1],
             [i for i in range(1, 101)], [i for i in range(101, 1, -1)],
             [i for i in range(1, 1000001)], [i for i in range(1000001, 1, -1)]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10))
