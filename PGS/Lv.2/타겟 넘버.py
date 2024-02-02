# n(트리의 상태) =  numbers 의 인덱스 
def dfs(n, total, numbers, target) :
    global answer, N 
    # 종료조건
    if n == N:
        if total == target :
            answer +=1
        return
    
    # 재귀 호출
    # 덧셈하는 경우
    dfs(n+1, total + numbers[n], numbers, target)
    # 뺄셈하는 경우
    dfs(n+1, total - numbers[n], numbers, target)

def solution(numbers, target):
    global answer, N
    answer = 0
    N = len(numbers)
    dfs(0, 0, numbers, target)
    
    return answer
