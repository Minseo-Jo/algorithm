from collections import deque

#입력
n, l, r = map(int, input().split())
A = []
for _ in range (n) :
    A.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

result = 0

def process(x,y,index):
    # 현재 위치(x,y)와 인접한 나라의 정보
    united = []
    united.append((x,y))
    q = deque([(x,y)])
    union[x][y] = index # 현재 연합 번호 할당
    sum_pop = A[x][y]
    sum_country = 1 

    #bfs 수행
    while q :
        x,y = q.popleft()
        for i in range (4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx  < n and 0 <= ny  < n and union[nx][ny] == -1:
                if l <= abs(A[x][y]-A[nx][ny]) <= r :
                    q.append((nx, ny))
                    # 같은 인덱스 번호로 연합 추가 표시 
                    union[nx][ny] = index
                    sum_pop += A[nx][ny]
                    sum_country +=1
                    united.append((nx, ny))
        
    # 연합 국가끼리 인구 분배
    for i,j in united :
        A[i][j] = sum_pop // sum_country
    return sum_country

# 인구 이동이 멈출 때까지 반복
while True :
    union = [[-1] * n for _ in range (n)]
    index = 0
    for i in range (n):
        for j in range (n):
            if union[i][j] == -1 : # 아직 처리 되지 않은 나라에서부터 bfs
                process(i,j,index)
                index += 1
    # 모든 나라의 인덱스가 달라서 인구 분배가 더이상 이루어지지 않는 경우 stop
    if index == n * n :
        break 
    result += 1

print(result)
