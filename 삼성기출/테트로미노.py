N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

# 가능한 모든 테트로미노 모양
tets = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # 1x4 형태 
        [(0,1), (1,0), (1,1)], # 2x2형태
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # ㄹ자 (회전)
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # ㄹ자 (대칭)
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # ㄴ자 (회전)
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # ㄴ자 (대칭)
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # ㅗ자(회전)
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
]

def calc(i,j,tet) :
    temp = arr[i][j] # 시작 위치는 범위 내 유효한 값
    for di,dj in tet :
        # 나머지 위치에 대해서는 범위 내 유효한지 검사
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0<= nj < M :
            temp += arr[ni][nj]
        else :
            return 0
    return temp


ans = 0
for i in range (N) :
    for j in range (M) :
        for tet in tets:
            temp = calc(i,j,tet) # 현재 위치에서 가능한 모든 모양의 합 계산
            ans = max(temp, ans)

print(ans)


# 두번째 풀이 dfs & 가지치기

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (N)]

v= [[0] * M for _ in range (N)] # dfs 방문 표시 배열

# 각 행에서 최대값을 찾은 뒤, 그 중 전체 배열의 최댓값을 찾음
mx = max(map(max, arr))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(n, temp, lst) :
    global ans

    # 가지치기 (ans 를 갱신 못해주는 경우)
    if temp + (4-n) * mx <= ans : # 나머지 블럭이 모두 최댓값이어도 현재 ans 값보다 작다면 dfs 순회 정지
        return 

    # 종료 조건
    if n == 4 :
        ans = max(temp, ans)
        return
    
    # 재귀 함수 호출 (기존 위치에서 뻗어나가기, 백트래킹)
    for cx, cy in lst :
        for i in range (4) :
            nx, ny = cx + dx[i], cy + dy[i]
            # 범위, 방문 검사
            if 0 <= nx < N and 0<= ny < M and v[nx][ny] == 0 :
                v[nx][ny] = 1
                dfs(n+1, temp + arr[nx][ny], lst + [(nx, ny)])
                v[nx][ny] = 0 # 방문표시 해제로 백트래킹

ans = 0
for i in range (N) :
    for j in range (M) :
        v[i][j] = 1
        dfs(1, arr[i][j], [(i,j)])

print(ans)
