import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# move_types sort해서 경로 순서가 사전순으로 나오도록
move_types = ['d', 'l', 'r', 'u'] #하, 좌, 우, 상 (사전순으로)
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
answer = 'z'

# N : 선택된 move_types의 개수 (경로 수열내의 인덱스)
def dfs(N, routes, n, m, x, y, r, c, k) :
    global answer
    # 가지치기
    if k < N + abs(x-r) + abs(y-c) :
        return
    #종료 조건 : 수열 인덱스가 k가 될 때
    if N == k and x == r and y == c :
        answer = routes
        return

    # 재귀 호출
    for j in range(4) :
        if 1 <= x + dx[j] <= n and 1 <= y + dy[j] <= m and routes + move_types[j] < answer: # 사전순으로 크다면 dfs 호출 x
            dfs(N + 1, routes + move_types[j], n, m, x + dx[j], y + dy[j], r, c, k)
            
def solution(n, m, x, y, r, c, k):
    #최단거리 계산
    dist = abs(x - r) + abs(y - c)
    if k - dist < 0 or (k - dist) % 2 == 1: 
        return "impossible"
    dfs(0, '', n, m, x, y, r, c, k)
    return answer
