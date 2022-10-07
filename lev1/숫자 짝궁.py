def solution(X, Y):
    X = sorted(list(X), reverse=True)
    Y = sorted(list(Y), reverse=True)
    XN, YN = len(X), len(Y)
    x_idx = y_idx = 0
    li = []
    while x_idx < XN and y_idx < YN:
        kx, ky = X[x_idx], Y[y_idx]
        if kx < ky: y_idx += 1
        elif kx > ky: x_idx += 1
        else:
            li.append(kx)
            x_idx += 1
            y_idx += 1
    if li:
        ans = "".join(li)
        return ans if ans[0] != "0" else "0"
    else:
        return "-1"


print(solution("100", "2345"))
print(solution("100", "5001111"))
