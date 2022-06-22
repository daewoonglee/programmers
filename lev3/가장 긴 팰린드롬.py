def solution(s):
    ans = 1
    for i in range(len(s)):
        for j in range(len(s)-1, i+1, -1):
            N = j-i
            b = 1 if N%2!=0 else 0
            if s[i: i+N//2+b] == s[i+N//2+1: j+1][::-1] and N >= ans: ans = N+1
    return ans


# print(solution("abcdcba")) # 7
# print(solution("abacde"))   # 3
# print(solution("aaaaabccbabb")) # 6
# print(solution("aaaaabcdcbabb")) # 7
print(solution("abcdefgh")) # 1
