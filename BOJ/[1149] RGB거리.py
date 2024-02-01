N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]

# 최소 비용을 저장하는 dp 테이블
dp = [[0] * 3 for _ in range (N)]

# dp 초기값 설정(첫번째 행은 그대로)
dp[0] = arr[0]

# 보텀업
for i in range (1, N) :
    # dp[i][color] : i번째 집을 color로 칠했을 때 총 최소 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0] #R로 색칠
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1] #G로 색칠
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2] #B로 색칠 

print(min(dp[N-1]))
