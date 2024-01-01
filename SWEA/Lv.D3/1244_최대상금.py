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


# 2 딕셔너리로 구현 (시간복잡도 최소화)
def dfs(n):
    global answer
    if n == change :
        answer = max(answer, int(''.join(map(str,lst))))
        return
    for i in range (L-1):
        for j in range (i+1, L) :
            lst[i],lst[j] = lst[j],lst[i]
            chk = int(''.join(map(str,lst)))
            if not visited.get((chk, n)) : # 방문하지 않았다면
                dfs(n+1)
                visited[(chk,n)]=True # 돌아오면서 방문 체크
            lst[i],lst[j] = lst[j],lst[i] # 원상복구 후 다른 조합 검사
                     

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers, change = input().split()
    lst = list(numbers)
    L = len(lst)
    change = int(change)
    answer = 0 #이전의 값과 비교하여 최댓값을 갱신할 수 있도록 변수 지정
    visited = {} # 백트래킹을 위한 방문 처리
    dfs(0) # 0회 교환부터 완전탐색 시작
    print(f'#{test_case} {answer}')
