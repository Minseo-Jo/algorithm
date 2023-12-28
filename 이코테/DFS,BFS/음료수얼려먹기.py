N, M = map(int, input().split())

graph = []
for _ in range (N) : 
   graph.append(list(map(int, input())))

def dfs(x, y):
   if x < 0 or x > N-1 or y < 0 or y > M-1 :
      return False
   
   if graph[x][y] == 0 : 
      graph[x][y] = 1

      # 상하좌우에 대해서 재귀호출
      dfs(x-1, y)
      dfs(x+1, y)
      dfs(x, y-1)
      dfs(x, y+1)
      return True
   
   return False


result = 0
for i in range(N):
   for j in range(M):
      if dfs(i,j) == True :
         result += 1

print(result)
