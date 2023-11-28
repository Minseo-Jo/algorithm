def solution(s):
    stack = []
    if (len(s) % 2 != 0 ) or (s[0] == ')') or (s[-1] == '('):
        return False
# 문자열 순회가 끝났을 때 stack이 모두 비워져야 짝지어서 괄호 닫기가 이루어진 것 
    for i in s : 
        if i == '(' :
            stack.append(i)
        else:
            if not stack : # 문자열 순회가 안끝났는데 stack이 비어있는 경우
                return False
            else : # i 가 ) 인 경우
                stack.pop()
    #문자열 순회가 끝났는데도 stack에 남아있는 경우
    if stack : 
        return False  
    return True

print(solution("(())))")) # False 