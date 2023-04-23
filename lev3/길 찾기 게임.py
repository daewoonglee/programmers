import sys
sys.setrecursionlimit(2000)


class Node(object):
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.val = v
        self.left = None
        self.right = None


def solution(nodeinfo):
    def init_tree():
        node_info_val = []
        for i, node in enumerate(nodeinfo):
            node_info_val.append([*node, i+1])
        node_info_val.sort(key=lambda x: (x[1], x[0]), reverse=True) # y, x 순으로 정렬

        root = Node(*node_info_val[0])
        for i in range(1, len(node_info_val)): # root에 해당하는 0번 인덱스 스킵
            t = root
            n = Node(*node_info_val[i])
            while 1:
                if t.x < n.x:
                    if t.right:
                        t = t.right
                    else:
                        t.right = n
                        break
                else:
                    if t.left:
                        t = t.left
                    else:
                        t.left = n
                        break

        return root

    def print_node(node, print_list, prefix=False):
        if node is None:
            return

        if prefix:
            print_list.append(node.val)
        print_node(node.left, print_list, prefix)
        print_node(node.right, print_list, prefix)
        if not prefix:
            print_list.append(node.val)

    root_tree = init_tree()
    pre_order, post_order = [], []
    print_node(root_tree, pre_order, prefix=True)
    print_node(root_tree, post_order, prefix=False)
    return [pre_order, post_order]

"""
1+2+4+8+16 = 31
1+2+4+8 = 15

edge 사이 관계 파악이 중요
y값 크기로 레벨 구분 (가장 큰 y가 루트 노드)
node level에 맞는 1차원 배열 생성 (2**0 + ... + 2**(n-1))
1차원 배열로 노드 정렬하여 접근 (left, right)
    1. empty node 배열은 비워둬야함, idx 시작은 1부터
    2. 가장 큰 y값을 1번 인덱스에 저장 (루트 노드)
    3. y-=1에 해당하는 값 탐색하여 저장
        3-1. 이전 노드 x보다 작으면 idx*2 (left)
        3-2. 이전 노드 x보다 크면 idx*2+1 (right)
    4. y=0이 될 때까지 3번 반복
    5. 전위, 후위 탐색

1 [5,3],
2 [11,5],
3 [13,3],
4 [3,5],
5 [6,1],
6 [1,3],
7 [8,6],
8 [7,2],
9 [2,2]
"""


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])) #[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
