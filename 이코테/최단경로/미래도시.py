n, m = map(int,input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경우에는 경로 비용 0으로 초기화
for a in range (1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0

# 간선 정보 입력받아 저장, 모든 비용은 1
for _ in range (m) :
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 반대방향도 초기화 해야함

# 도착지(x) 거쳐가는 지점(k) 입력
x, k = map(int, input().split())

# 플루이드워셜로 1~k, k~x까지 가는데 최단경로 탐색
for i in range (1, n+1):
    graph[1][k] = min(graph[1][k], graph[1][i]+graph[i][k])
    graph[k][x] = min(graph[k][x], graph[k][i] + graph[i][x])

if graph[1][k] == INF or graph[k][x] == INF :
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
