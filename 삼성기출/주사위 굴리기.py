n, m, x, y, k = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

command = list(map(int, input().split()))

dice = [0,0,0,0,0,0] #밑, 뒤, 우, 좌, 앞, 위
#동(1), 서(2), 북(3), 남(4)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def turn(direction) : 
    # 주사위의 인덱스는 주사위 위치를 나타냄
    # 알파벳은 주사위 번호(1~6)
    a,b,c,d,e,f = dice[0],dice[1], dice[2], dice[3], dice[4], dice[5]

    if direction == 1: #동쪽
        dice[0],dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif direction == 2: #서쪽
        dice[0],dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c 
    elif direction == 3 : #북쪽
        dice[0],dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e
    else : # 남쪽
        dice[0],dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b


# 명령에 따라 시뮬레이션 시작
for i in command :
    nx, ny = x + dx[i-1], y + dy[i-1] # 좌표 변경
    # 주사위가 맵을 벗어났을 때
    if nx < 0 or nx >= n or ny < 0 or ny >= m :
        #명령무시, 위치 이전으로 돌려놔야함
        nx, ny = nx - dx[i-1], ny - dy[i-1]
        continue
    turn(i) # 주사위 방향 바꾸고
    # 맵정보 검사
    if graph[nx][ny] == 0 :
        graph[nx][ny] = dice[0] # 주사위 밑의 값 복사
    else :
        dice[0] = graph[nx][ny] # 맵의 값을 주사위 밑으로 복사
        graph[nx][ny] = 0
    # 다음 위치 값 갱신
    x, y = nx, ny
    # 매번 명령마다 주사위 윗면 출력
    print(dice[5])
