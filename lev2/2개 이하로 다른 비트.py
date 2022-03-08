def solution(numbers):
    # 0.09341625805245712
    #ans = []
    #for n in numbers:
    #    n = int(n) # 문제에선 양의 정수라고 하지만 int 안해주면 런타임 에러 발생
    #    bin_n = bin(n)[2:]
    #    if n >= 3 and bin_n[-1] == "1" and bin_n[-2] == "1":
    #        idx = len(bin_n) - (3 if len(bin_n) > 3 else 2)
    #        while idx > 0:
    #            if bin_n[idx] != "1":
    #                break
    #            idx -= 1
    #        m = 1 if idx == 0 else 2
    #        ans.append(int(bin_n[:idx] + "10" + bin_n[idx+m:], 2))
    #    else:
    #        ans.append(n+1)
    #return ans
   
    # code refactoring - 0.07790907996241003
    #ans = []
    #for n in numbers:
    #    n = int(n)
    #    if n & 1:
    #        target = n
    #        idx = 0
    #        while n > 0:
    #            if n % 2 == 0:
    #                break
    #            n //= 2
    #            idx += 1
    #        ans.append(target + 2 ** idx - 2 ** (idx-1))
    #    else:
    #        ans.append(n+1)
    #return ans

    # code refactoring 02 - 0.028094679990317672
    return [((n ^ (n+1)) >> 2) + n + 1 for n in numbers]
    

print(solution([2,7]))
print(solution([11,15,19,23]))
print(solution([0,1,3]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[2,7], [11,15,19,23], [0,1,3], [1000,100000,10**7,10**15]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))

