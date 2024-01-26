from collections import deque
import sys

input = sys.stdin.readline3


def bfs(before, after) :
    q = deque([('',before)])

    while q :
        command, before = q.popleft()
        
        if before == after :
            print(command)
            break

        for i in ['D', 'S', 'L', 'R'] :
            if i == 'D' :
                before2 = before * 2 % 10000
    
            if i == 'S' :
                before2 = (before - 1) % 10000
            
            if i =='L' :
                before2 = before // 1000 + (before % 1000)*10
            
            if i == 'R' :
                before2 = before // 10 + (before % 10) * 1000

            if before2 not in visited :
                q.append((command + i, before2))
                visited.add(before2)

T = int(input())
for t in range (T) :
    before, after = map(int,(input().split()))
    visited = set()
    bfs(before, after)
