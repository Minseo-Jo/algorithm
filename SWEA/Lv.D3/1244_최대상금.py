def dfs(n):
    global ans
    if n==N:
        ans = max(ans, int("".join(map(str,lst))))
        return
 
    # L개에서 2개뽑는 모든 조합(둘을 교환)
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]
 
            chk = int("".join(map(str,lst)))*10+n
            if chk not in v:
                dfs(n+1)
                v.append(chk) # 노드 방문 후 체크
 
            lst[i], lst[j] = lst[j], lst[i] # 원상복구 후 다른 조합 검사
 
T = int(input())
for test_case in range(1, T + 1):
    number, n = input().split()
    N = int(n)
    lst = list(number)
    L = len(lst)
    ans = 0
    v = []
    dfs(0)
    print(f'#{test_case} {ans}')
