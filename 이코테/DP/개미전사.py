n = int(input())

array = list(map(int, input().split()))

dp = [0] * 100 
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+array[i]) # i번째 식량창고 선택안하는 경우 or 선택 하는 경우 중 최대값 저장


print(dp[n-1])
