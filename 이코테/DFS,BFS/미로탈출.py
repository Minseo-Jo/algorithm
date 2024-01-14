from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range (n) :
    graph.append(list(map(int, input())))


dx = [0,-1,1,0]
dy = [1,0,0,-1]

def bfs():
    x, y = 0,0
    q = deque([(x,y)])
    while q :
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i] , cy+dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[nx][ny] == 1 :
                graph[nx][ny] = graph[cx][cy] + 1
                q.append((nx,ny))
            else:
                continue

    return graph[n-1][m-1]

print(bfs())
