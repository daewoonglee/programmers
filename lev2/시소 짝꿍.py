from collections import Counter


def solution(weights):
    w_dict = Counter(weights)
    dist = [2/3, 2, 3/4]
    # ans = 0
    # for w, v in w_dict.items():
    #     # 0.377581197
    #     if v > 1:
    #         ans += (v - 1) * v // 2
    #     ans += sum([w_dict[w*d]*v for d in dist if w*d in w_dict])
    #
    #     # # without if - 0.357757928
    #     # ans += sum([w_dict[w*d]*v for d in dist if w*d in w_dict]) + (v - 1) * v // 2
    # return ans

    # # code refactoring, comprehension - 0.36814881499999996
    return sum([sum([w_dict[w*d]*v for d in dist if w*d in w_dict]) + (v - 1) * v // 2 for w, v in w_dict.items()])


# print(solution([100,180,360,100,270])) # 4
# print(solution([100,110])) # 0
# print(solution([100,100])) # 1
# print(solution([100,100,200])) # 3
# print(solution([100,100,100])) # 3
# print(solution([100,100,100,100])) # 6
# print(solution([100,100,100,100,100])) # 10
# print(solution([100,100,100,100,100,100])) # 15
# print(solution([100,110,300,200])) # 2
print(solution([100,200,100,200,100,200])) # 15


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [100,180,360,100,270],
        [100,110],
        [100,100,100,100,100,100],
        [100,200,100,200,100,200],
        [100,200,100,200,100,200]*100,
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
