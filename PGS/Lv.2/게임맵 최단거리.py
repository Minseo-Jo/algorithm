from collections import deque

#좌, 우, 상, 하
dx = [-1,1,0,0]
dy = [0, 0, -1, 1]

def bfs(maps, n, m, answer) :
    q = deque([(0,0)])
    
    while q :
        cx, cy = q.popleft()
        
        for i in range (4) :
            nx, ny = cx + dx[i] , cy + dy[i]
            
            if 0<= nx < n and 0 <= ny < m and maps[nx][ny] == 1 :
                q.append((nx, ny))
                maps[nx][ny] = maps[cx][cy] + 1 # 맵자체에 최단 경로값을 기록!
            else :
                continue

    answer = maps[n-1][m-1]
            
    if answer == 1 :
        return -1
    else :
        return answer
                

def solution(maps):
    n = len(maps) # 행 길이
    m = len(maps[0]) # 열 길이
    
    answer = 1
    answer = bfs(maps, n, m, answer)
    return answer
