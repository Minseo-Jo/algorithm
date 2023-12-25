N = int(input())
plans = list(input().split())

x,y  = 1,1

dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_types = ['R', 'L', 'U', 'D']

for plan in plans :
    for i in range (len(move_types)):
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시        
    if nx < 1 or ny < 1 or nx > N or ny > N :
        continue
    else : # 벗어나지 않는다면 이동
        x, y = nx, ny 
    
print(x, y)
