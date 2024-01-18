N = int(input())
ans = 0
# 열 방문 체크 
v1 = [0] * N
# 위쪽 대각선 방문 체크
v2 = [0] * (2*N)
v3 = [0] * (2*N)


def dfs(n) : # n은 행의 번호
    global ans
    # 종료 조건
    if n == N :
        ans +=1
        return
    # 재귀 함수 호출
    for j in range (N) : # 열을 선택할 수 있는 경우의 수 N-1 개
        if v1[j] == v2[n+j] == v3[n-j] == 0: # 가능 조건 검사
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0 

dfs(0)
print(ans)
