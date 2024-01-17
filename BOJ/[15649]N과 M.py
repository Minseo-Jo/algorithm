import sys
input = sys.stdin.readline()

N, M = map(int,input.split())


def dfs(n, lst): # n(선택된 숫자의 개수) 가 노드의 상태를 나타냄
    # 종료조건
    if n == M : # 선택된 숫자의 개수가 M과 같아질 때
        ans.append(lst)
        return
    
    # 재귀 호출
    for j in range (1, N+1) : # 다음 숫자로 선택할 수 있는 경우의 수 N개
        if v[j] == 0 : # 중복 방지를 위해 visited 검사
            v[j] = 1 
            dfs(n+1, lst + [j]) # 선택된 숫자 추가해서 다음 단계 재귀 호출
            v[j] = 0 # 다시 복구 후 dfs 수행해야함


ans = []
# 방문 표시
v = [0] * (N+1)
dfs(0, [])
for lst in ans :
    print(*lst)
