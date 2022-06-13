import heapq

class max_heap():
    # built max heap using a list
    def __init__(self):
        self.works = [None]

    def __getitem__(self, idx):
        return self.works[idx]

    def __len__(self):
        return len(self.works)

    def swap(self, p, c):
        t = self.works[p]
        self.works[p] = self.works[c]
        self.works[c] = t

    def push(self, val):
        self.works.append(val)
        idx = len(self.works)-1
        while idx != 1:
            left = idx//2
            right = idx//2+1
            if self.works[left] < self.works[idx]:
                self.swap(left, idx)
                idx = left
            elif self.works[right] < self.works[idx]:
                self.swap(right, idx)
                idx = right
            else:
                break

    def pop(self):
        return self.works.pop(1)


def solution(n, works):
    if sum(works) <= n: return 0

    # 3.0135803930000002
    # works = [-w for w in works]
    # heapq.heapify(works)
    # for _ in range(n):
    #     heapq.heappush(works, heapq.heappop(works)+1)
    # return sum([(w*w) for w in works])

    # 15.065884422
    mh = max_heap()
    for w in works:
        mh.push(w)

    for _ in range(n):
        val = mh.pop() - 1
        mh.push(val)

    return sum([v**2 for v in mh[1:]])


# print(solution(4,[4,3,3])) # 12
# print(solution(1,[2,1,2])) # 6
# print(solution(3,[1,1]))   # 0
# print(solution(7,[10,9,3,3,3])) # 99
print(solution(99,[2,15,22,55,55])) # 580
print(solution(2,[8])) # 36


if __name__ == "__main__":
    from timeit import Timer
    query = [[99,[2,15,22,55,55]],
             [9999, [2222, 15000, 22000, 49999, 49999]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=1000))
