N, M = map(int, input().split())
ans = []

def dfs(n, start, lst) :
    #종료 조건
    if n == M :
        ans.append(lst)
        return
    
    for i in range (start, N+1) :
        dfs(n+1, i, lst+[i]) # start = i로 호출!!


dfs(0,1,[])
for answer in ans :
    print(*answer)
