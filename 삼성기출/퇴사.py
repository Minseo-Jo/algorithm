# 풀이 1) 완전탐색(백트래킹)
N = int(input())

# 상담기간(t), 수익(p)
t,p = [],[]

for _ in range (N):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


def dfs(n, sm) :
    global ans
    # 종료 조건
    if n >= N:
        ans = max(ans, sm) # ans 갱신
        return
    
    # 재귀 함수 호출 
    # 경우 1) 상담을 하는 경우 (퇴사일 전 완료 가능할 때만)
    if n + t[n] <= N :
        dfs(n+t[n], sm+p[n])
    # 경우 2) 상담을 안 하는 경우 (모든 경우에서 가능함)
    dfs(n+1, sm)

ans = 0
dfs(0,0)
print(ans)



#문제 풀이 2) DP 로 푸는 경우
N = int(input())

# 상담기간(t), 수익(p)
t,p = [],[]

for _ in range (N):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# dp 테이블 초기화
dp = [0] * (N+1)

# 뒤부터 접근
for n in range (N-1, -1, -1):
    #상담 가능하다면 (퇴사일 내 가능하다면)
    if n + t[n] <= N :
        # 상담o, 상담x 경우 비교
        dp[n] = max(dp[n+1], dp[n+t[n]]+ p[n])
    # 상담 불가능하다면
    else : 
        # 이후 날짜의 최대 수익 값 그대로(dp테이블 n+1로 초기화해 준 이유)
        dp[n] = dp[n+1] 

print(dp[0])
