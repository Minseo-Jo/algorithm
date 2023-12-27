# N : 맵의 행, M : 맵의 열
N, M = map(int, input().split())

# 방문한 위치 지정을 위한 행렬
d = [[0]* M for _ in range(N)]
x, y, direction = map(int, input().split())
# 현재 위치 방문 처리
d[x][y] = 1


# 전체 맵 정보 받기
array = []
for i in range (N):
    array.append(list(map(int, input().split())))

# 북 동 남 서 (시계열 반대 방향으로) 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수 정의 
def turn_left():
    global direction # 함수 밖에서 정의된 direction 변수를 사용하기 위해 전역 변수로 
    direction -= 1 
    if direction == -1 :  # 북 -> 서로 회전할 때 방향 인덱스 0->3으로 가야함
        direction = 3

count = 1
turn_time = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 아직 안 가본 곳이거나 바다가 아니라면 앞으로 전진
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue # 전진하고 다시 리셋

    else : # 이미 가봤거나 바다라면 회전
        turn_time += 1

    if turn_time == 4 : # 네 방향 다 가지 못한다면
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0 : # 뒤로 가기
            x = nx
            y = ny
        else : # 바다로 막혀있는경우 
            break
        turn_time = 0 
print(count)
