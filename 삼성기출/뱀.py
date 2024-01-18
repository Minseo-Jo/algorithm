n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

#사과 위치(1) 표시
for _ in range (k) :
    x, y = map(int, input().split())
    graph[x][y] = 1

l = int(input())
info = [] # 위치 정보 리스트

for _ in range (l) :
    t, c = input().split()
    info.append((int(t), c))


# 뱀은 동쪽부터 이동
# 동(0), 남(1), 서(2), 북(3)
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 회전 함수
def turn(direction, c):
    #만약 L 회전이면 방향 -1
    if c == 'L' : 
        direction = (direction - 1) % 4
    # D 회전이면 방향 +1 
    else :
        direction = (direction + 1) % 4
    return direction

# 시뮬레이션 함수
def simulation(graph) :
    x, y = 1,1 # 뱀의 초기 머리 위치
    direction = 0 # 뱀의 초기 방향(북)
    time, index = 0,0 # 시간, 방향정보를 나타내는 index
    graph[x][y] = 2 # 뱀의 현재 위치(2) 표시
    q = [(x,y)] # 뱀의 위치를 나타내주는 리스트 (꼬리가 첫번쨰 요소)

    # 시뮬레이션 시작
    while True:
        nx, ny = x + dx[direction], y+dy[direction]
        # 게임 종료 조건 검사
        if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 2: 
            # 사과가 없다면
            if graph[nx][ny] == 0:
                q.append((nx, ny)) # 현재 위치 정보 업데이트
                px, py = q.pop(0) # 꼬리 위치는 삭제
                graph[px][py] = 0 # 그래프 위치 정보 업데이트
                graph[nx][ny] = 2
                x, y = nx, ny # 머리 이동
                time += 1
            # 사과가 있다면
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 2
                x, y = nx, ny
                time += 1
        # 게임이 종료되면
        else :
            time +=1
            break

        # 방향을 전환해야되면
        if index < l and time == info[index][0] :
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulation(graph))
