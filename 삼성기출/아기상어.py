from collections import deque
INF = 1e9
n = int(input())

array = []
for _ in range (n) :
    array.append(list(map(int, input().split())))

# 초기 아기 상어 크기, 위치 변수
now_size=2
now_x, now_y = 0,0

# 아기 상어 위치 초기화
for i in range(n):
    for j in range (n):
        if array[i][j] == 9:
            now_x, now_y = i,j
            array[now_x][now_y] = 0

# 우선순위 위 -> 왼
dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 모든 위치까지의 최단거리 계산
def bfs():
    # 도달할 수 없는 공간은 -1
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0 # 현재 위치는 거리 0
    # bfs 수행
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n : 
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size :
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


# 최단 거리 중 먹을 물고기 찾기
def find(dist) :
    x, y = 0,0
    min_dist = INF
    for i in range (n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist :
                    x, y = i,j
                    min_dist = dist[i][j]
    
    if min_dist == INF : 
        return None
    else:
        return x, y, min_dist
    

result = 0
# 먹은 물고기 개수 
ate = 0
while True :
    # 먹을 수 있는 물고기 찾기
    value = find(bfs())
    # 먹을 물고기가 더이상 없다면 stop
    if value == None :
        print(result)
        break

    else : 
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 물고기 먹은 위치는 0으로 초기화
        array[now_x][now_y] = 0
        ate += 1 
        if ate >= now_size :
            now_size += 1
            ate = 0
