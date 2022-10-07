def solution(X, Y):
    # # 0.19265791300000001
    # X = sorted(list(X), reverse=True)
    # Y = sorted(list(Y), reverse=True)
    # XN, YN = len(X), len(Y)
    # x_idx = y_idx = 0
    # li = []
    # while x_idx < XN and y_idx < YN:
    #     kx, ky = X[x_idx], Y[y_idx]
    #     if kx < ky: y_idx += 1
    #     elif kx > ky: x_idx += 1
    #     else:
    #         li.append(kx)
    #         x_idx += 1
    #         y_idx += 1
    # if li:
    #     ans = "".join(li)
    #     return ans if ans[0] != "0" else "0"
    # else:
    #     return "-1"

    # code refactoring - 0.124140364
    li = []
    for i in set(X):
        m = min(X.count(i), Y.count(i))
        if m: li.append(i)
    if not li: return "-1"
    li.sort(reverse=True)
    ans = "".join(li)
    return "0" if ans[0] == "0" else ans



print(solution("100", "2345"))
print(solution("100", "5001111"))


if __name__ == "__main__":
    from timeit import Timer
    query = [["123","110"],["100000000", "10000000"], ["222","10001"], ["3000000", "1231234"], ["300", "123"],
             ["3033", "12325894"], ["3000000", "1231235"], ["1230000", "45678987"]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
