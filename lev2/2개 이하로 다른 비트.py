def solution(numbers):
    ans = []
    for n in numbers:
        bin_n = bin(n)[2:]
        if bin_n[-1] == "1" and bin_n[-2] == "1":
            idx = len(bin_n)-3
            while idx > 0:
                if bin_n[idx] != "1":
                    break
                idx -= 1
            m = 1 if idx == 0 else 2
            ans.append(int(bin_n[:idx] + "10" + bin_n[idx+m:], 2))
        else:
            ans.append(n+1)
    return ans


print(solution([2,7]))
print(solution([11,15,19,23]))

