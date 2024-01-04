from collections import deque

INF = 10000 
def bfs(sx,sy,ex,ey):
    q = deque()
    v = [[INF]*N for _ in range(N)] #비용 그래프 초기화
    q.append((sx,sy))
    v[sx][sy] = 0
    while q:
        cx,cy = q.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range (4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 범위 내 존재, 이동할 위치의 비용이 더 큰 경우에만 queue 삽입
            if 0 <= nx < N and 0<= ny < N and v[nx][ny] > v[cx][cy] + arr[nx][ny] :
                q.append((nx,ny))
                v[nx][ny] = v[cx][cy] + arr[nx][ny] # 최소값으로 갱신
    return v[ex][ey]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = bfs(0,0,N-1,N-1)
    print (f'#{test_case} {ans}')
