def solution(want, number, discount):
    # # 13.462309007
    # w_dict = {k: v for k, v in zip(want, number)}
    #
    # d_dict = dict()
    # for i in range(10):
    #     if discount[i] not in d_dict: d_dict[discount[i]] = 1
    #     else: d_dict[discount[i]] += 1
    # ans = int(w_dict == d_dict)
    #
    # for i in range(1, len(discount)-9):
    #     if d_dict[discount[i-1]] > 1: d_dict[discount[i-1]] -= 1
    #     else: del d_dict[discount[i-1]]
    #     if discount[i+9] not in d_dict: d_dict[discount[i+9]] = 1
    #     else: d_dict[discount[i+9]] += 1
    #
    #     ans += int(w_dict == d_dict)
    # return ans

    # code refactoring - 8.146081137
    w_hash = sum([hash(w) * number[i] for i, w in enumerate(want)])
    d_hash = sum([hash(discount[i]) for i in range(10)])
    ans = int(w_hash == d_hash)

    for k in range(len(discount)-10):
        d_hash += -hash(discount[k]) + hash(discount[k + 10])
        ans += int(w_hash == d_hash)
    return ans


# print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) # 3
# print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])) # 0
# print(solution(["a", "aa"], [8, 2], ["aa"] + ["a"]*10 + ["aa", "aa"] + ["a"]*10))
print(solution(["a"], [10], ["a"]*1000))
print(solution(["a", "b"], [5, 5], ["a", "b"]*1000))


if __name__ == "__main__":
    from timeit import Timer
    import random
    r = [i for i in range(1, 101)]
    r1 = r[:50]
    random.shuffle(r)
    random.shuffle(r1)
    query = [[["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]],
             [["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]],
             [["a", "aa"], [8, 2], ["aa"] + ["a"]*10 + ["aa", "aa"] + ["a"]*10],
             [["a"], [10], ["a"]*1000],
             [["a", "b"], [5, 5], ["a", "b"]*1000]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
