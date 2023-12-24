N, M, K = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse=True)

#풀이 1)
while True :
    for i in range (K):
        if M == 0 :
            break
        else: 
            result += data[0]
            M -= 1
    if M == 0 :
        break
    else :
        result += data[1]
        M -= 1
    
print(result)

# 풀이 2) 시간 효율성을 고려한 풀이
# 가장 큰 수가 더해지는 횟수 구하기
count = M//(K+1) * K + M % (K+1)

result += count * data[0]
result += (M-count) * data[1] # 큰 수를 더하고 남은 횟수는 두 번째로 큰 숫자 더하기

print(result)
