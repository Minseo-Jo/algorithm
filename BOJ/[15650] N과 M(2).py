# 이진 트리로 푸는 법
N, M = map(int, input().split())
ans = []

# n : 선택할 숫자
def dfs(n, lst) : 
    # 종료 조건
    if n > N : 
        # 정답 갱신
        if len(lst) == M :
            ans.append(lst)
        return
    
    # 재귀 호출
    dfs(n+1, lst + [n]) # n을 선택했을 경우
    dfs(n+1, lst) # n을 선택하지 않았을 경우

dfs(1, [])
for lst in ans :
    print(*lst)


# 멀티 트리로 푸는 법
N, M = map(int, input().split())
ans = []

# n : 선택된 원소의 개수, s: 선택할 숫자 시작점
def dfs(n, s, lst) :
    # 종료 조건
    if n == M : 
        ans.append(lst) 
        return
    
    # 재귀 호출
    for i in range(s, N+1) :
        dfs(n+1, i+1, lst + [i])

dfs(0, 1, [])
for lst in ans :
    print(*lst)
