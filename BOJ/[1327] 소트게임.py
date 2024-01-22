from collections import deque

n,k = map(int, input().split())
arr = list(input().split()) # 문자열 변환을 위해 int형으로 매핑 x
target = sorted(arr)
visited = set("".join(arr)) # 뒤집어봤던 배열 저장 set, 문자열로 변환해서 넣어줘야함
ans = -1

def bfs(arr, cnt) :
    global ans
    q = deque([(arr, cnt)])

    while q :
        arr, cnt = q.popleft()

        if arr == target :
            ans = cnt
            break

        for i in range(n-k+1) : # 뒤집기가 가능한 범위까지
            temp = arr[i : i+k]
            temp.reverse()
            arr2 = arr[:i] + temp + arr[i+k:]
            str2 = "".join(arr2)
            
            if str2 not in visited : 
                q.append((arr2,cnt+1)) # 큐에 저장해서 해당 배열 내에서 인덱스 0부터 돌아가면서 뒤집어보기
                visited.add(str2) 

bfs(arr, 0)
print(ans)
