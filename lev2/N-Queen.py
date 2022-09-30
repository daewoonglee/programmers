def solution(n):
    def search_queen(idx, col):
        global ans
        if len(col) == n:
            ans += 1
        else:
            for i in range(n):
                if i in idx or i in col: continue
                search_queen([i, i - 1, i + 1], col + [i])
    global ans
    ans = 0
    for i in range(n):
        columns = [i]
        search_queen([i, i-1, i+1], columns)
    return ans


# print(solution(4)) # 2
print(solution(5)) # 5


"""
(포인트) 선택된 범위 제거한 리스트를 어떻게 만들 수 있는가?

    for d in range(n): 
        mat[i][d]=1 # 가로
        mat[d][j]=1 # 세로        
    왼위: for d in range(1,j): mat[i-d][j-d]=1
    왼아: for d in range(1,n-i): mat[i+d][j+d]=1
    오위: for d in range(1,n-j): mat[i-d][j+d]=1
    오아: for d in range(1,n-j): mat[i+d][j+d]=1

    사선 처리에 대한 일반화 수식을 못만들고있음, 현재 접근 방법으론 모든 경우의 수 처리 불가
    
    사선에 대한 경우의 수를 어떻게 구할 것인가?
        규칙을 찾아야 함 / 어떻게 탐색을 할 것인지
    
    n=3 (0,1) = (1,2) (2,3)
        (1,0) = (0,1) (2,1)
    
    n=5 (3,1) = (2,0) / (4,2) / (4,0) / (0,4) (1,3) (2,2)
        (3,1) = (0,4) (1,3) (2,0) (2,2) (4,0) (4,2)
        
    n=7 (4,5) = (0,1) (1,2) (2,3) (3,4) / (5,6) / (3,6) / (5,4) (6,3)
        (4,5) = (0,1) (1,2) (2,3) (3,4) (3,6) (5,4) (5,6) (6,3)
        
        
        
"""
