def solution(lottos, win_nums):
    # 0.07922274805605412
    #lottos.sort(reverse=True)
    #win_nums.sort(reverse=True)
    #
    #zeros = len([l for l in lottos if not l])
    #N = len(lottos)
    #matched = l_idx = w_idx = 0
    #while l_idx < N and w_idx < N:
    #    if lottos[l_idx] < win_nums[w_idx]:
    #        w_idx += 1
    #    elif lottos[l_idx] > win_nums[w_idx]:
    #        l_idx += 1
    #    else:
    #        matched += 1
    #        w_idx += 1
    #        l_idx += 1
    #return [7-matched-zeros if matched or zeros else 6, 7-matched if matched else 6]

    # code refactoring - 0.03896871209144592
    #rank = [6, 6, 5, 4, 3, 2, 1]
    #zeros = lottos.count(0)
    #matched = 0
    #for n in win_nums:
    #    if n in lottos:
    #        matched += 1
    #return [rank[zeros+matched], rank[matched]]

    # code refactoring 02 - 0.044579632580280304
    rank = [6, 6, 5, 4, 3, 2, 1]
    zeros = lottos.count(0)
    matched = len(set(lottos) & set(win_nums))
    return [rank[zeros+matched], rank[matched]]


print(solution([44,1,0,0,31,25], [31,10,45,1,6,19]))
print(solution([0,0,0,0,0,0], [38,19,20,40,15,25]))
print(solution([45,4,35,20,3,9], [20,9,3,45,4,35]))
print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))


if __name__ == "__main__":
    from timeit import Timer
    query = [[[44,1,0,0,31,25], [31,10,45,1,6,19]], [[0,0,0,0,0,0], [38,19,20,40,15,25]], [[45,4,35,20,3,9], [20,9,3,45,4,35]], [[1,2,3,4,5,6], [7,8,9,10,11,12]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

