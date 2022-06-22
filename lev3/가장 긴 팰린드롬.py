def solution(s):
    # 1.459431129
    # ans = 1
    # for i in range(len(s)):
    #     for j in range(len(s)-1, i+1, -1):
    #         N = j-i
    #         b = 1 if N%2 != 0 else 0
    #         if s[i: i+N//2+b] == s[i+N//2+1: j+1][::-1] and N >= ans: ans = N+1
    # return ans

    # code refactoring - 1.086260714
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i


# print(solution("abcdcba")) # 7
# print(solution("abacde"))   # 3
print(solution("aaaaabccbabb")) # 6
# print(solution("aaaaabcdcbabb")) # 7
# print(solution("abcdefgh")) # 1


if __name__ == "__main__":
    from timeit import Timer
    query = ["abcdcba", "abacde", "aaaaabccbabb", "aaaaabcdcbabb", "abcdefgh", "aaaabcdcbab"*20]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=100))
