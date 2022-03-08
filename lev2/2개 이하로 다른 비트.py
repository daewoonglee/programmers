def solution(numbers):
    ans = []
    for n in numbers:
        n = int(n) # 문제에선 양의 정수라고 하지만 int 안해주면 런타임 에러 발생
        bin_n = bin(n)[2:]
        if n >= 3 and bin_n[-1] == "1" and bin_n[-2] == "1":
            idx = len(bin_n) - (3 if len(bin_n) > 3 else 2)
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
print(solution([0,1,3]))

