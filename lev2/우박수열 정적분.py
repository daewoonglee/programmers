def solution(k, ranges):
    def collatz(n):
        li = [n]
        while n > 1:
            n = n//2 if n % 2 == 0 else n*3+1
            li.append(n)
        return li

    collatz_list = collatz(k)
    N = len(collatz_list)
    print(collatz_list)
    area = [(cl + collatz_list[i+1])/2 for i, cl in enumerate(collatz_list[:-1])]
    print(area)

    ans = []
    for i in ranges:
        if i[0] == N+i[1]-1 < 0:
            ans.append(0.)
        elif i[0] > N+i[1]-1:
            ans.append(-1.)
        else:
            if i[1] == 0:
                ans.append(sum(area[i[0]:]))
            else:
                ans.append(sum(area[i[0]:i[1]]))
    return ans



"""
사다리꼴 = (밑변+윗변)*높이/2
밑변 = f(x1)
윗변 = f(x2)
높이 = 1
(collatz_list[i] + collatz_list[i+1]) / 2
"""


print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]])) # [33.0,31.5,0.0,-1.0]
