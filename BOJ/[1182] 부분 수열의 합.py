N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

# dfs의 노드 (n)는 배열의 인덱스
def dfs(n, sum, cnt) :
    global ans

    if n == N : # 배열의 인덱스가 N이 된다면 모든 원소의 포함여부를 다 검사한 것
        if sum == S and cnt > 0 : # 원소는 적어도 하나 이상 포함되어야함
            ans += 1 
        return #return 들여쓰기 주의할 것
        
    # 재귀 함수 
    # 원소를 포함하는 경우
    dfs (n+1, sum + arr[n], cnt + 1)
    # 원소 포함 안하는 경우
    dfs(n+1, sum, cnt)

dfs(0,0,0)
print(ans)
