from datetime import timedelta
import math


def solution(fees, records):
    ans = {}
    stack = {}
    fin = timedelta(minutes=59, hours=23)
    for r in records:
        rt, rn, rio = r.split()
        if rn not in stack:
            stack[rn] = list()
        if rio == "IN":
            stack[rn].append(rt)
        else:
            in_h, in_m = stack[rn].pop().split(":")
            in_t = timedelta(hours=int(in_h), minutes=int(in_m))
            out_h, out_m = rt.split(":")
            out_t = timedelta(hours=int(out_h), minutes=int(out_m))
            if rn not in ans:
                ans[rn] = 0
            ans[rn] += (out_t-in_t).total_seconds()
    for k, v in stack.items():
        if v:
            if k not in ans:
                ans[k] = 0
            h, m = v[0].split(":")
            ans[k] += (fin-timedelta(hours=int(h), minutes=int(m))).total_seconds()
    
    answer = []
    basic_t, basic_c, unit_t, unit_c = fees
    basic_t *= 60
    unit_t *= 60
    for k in sorted(ans, key=lambda x: int(x[0])):
        if ans[k] <= basic_t:
            answer.append(basic_c)
        else:
            answer.append(basic_c + (math.ceil((ans[k]-basic_t)/unit_t) * unit_c))
    return answer
            

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))


