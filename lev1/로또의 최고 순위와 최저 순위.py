def solution(lottos, win_nums):
    lottos.sort(reverse=True)
    win_nums.sort(reverse=True)
    
    zeros = len([l for l in lottos if not l])
    N = len(lottos)
    matched = l_idx = w_idx = 0
    while l_idx < N and w_idx < N:
        if lottos[l_idx] < win_nums[w_idx]:
            w_idx += 1
        elif lottos[l_idx] > win_nums[w_idx]:
            l_idx += 1
        else:
            matched += 1
            w_idx += 1
            l_idx += 1
    return [7-matched-zeros if matched or zeros else 6, 7-matched if matched else 6]


print(solution([44,1,0,0,31,25], [31,10,45,1,6,19]))
print(solution([0,0,0,0,0,0], [38,19,20,40,15,25]))
print(solution([45,4,35,20,3,9], [20,9,3,45,4,35]))
print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))


