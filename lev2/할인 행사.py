def solution(want, number, discount):
    def is_same():
        # print(f"dk: {d_keys}, d_dict: {d_dict}")
        if len(w_keys) != len(d_keys): return 0
        for wk, dk in zip(w_keys, d_keys):
            if not(wk == dk and w_dict[wk] <= d_dict[dk]): return 0
        return 1

    ans = 0
    w_dict = {k: v for k, v in zip(want, number)}
    w_keys = sorted(w_dict)
    # print(f"wk: {w_keys}, w_dict: {w_dict}")
    d_dict = dict()
    for i in range(10):
        if discount[i] not in d_dict: d_dict[discount[i]] = 1
        else: d_dict[discount[i]] += 1
    d_keys = sorted(d_dict)
    ans += is_same()

    for i in range(1, len(discount)-9):
        if d_dict[discount[i-1]] > 1: d_dict[discount[i-1]] -= 1
        else: del d_dict[discount[i-1]]
        if discount[i+9] not in d_dict: d_dict[discount[i+9]] = 1
        else: d_dict[discount[i+9]] += 1

        d_keys = sorted(d_dict)
        ans += is_same()
    return ans


# print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) # 3
# print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])) # 0
print(solution(["a", "aa"], [8, 2], ["aa"] + ["a"]*10 + ["aa", "aa"] + ["a"]*10))
