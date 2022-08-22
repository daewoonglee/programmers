def solution(survey, choices):
    li = "RTCFJMAN"
    scores = [3, 2, 1, 0, 1, 2, 3]
    cnt = {k: 0 for k in li}
    for s, c in zip(survey, choices):
        if c < 4: cnt[s[0]] += scores[c-1]
        elif c > 4: cnt[s[1]] += scores[c-1]
    ans = [li[i*2] if cnt[li[i*2]] >= cnt[li[i*2+1]] else li[i*2+1] for i in range(4)]
    return "".join(ans)


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # RCJA
 