L, C = map(int, input().split())
candidate = list(input().split())
candidate.sort()
ans = []

def count_vowel(code) :
    cnt = 0
    vowel = ['a', 'e', 'i', 'o', 'u']

    for i in code :
        if i in vowel :
            cnt += 1

    return cnt

def dfs(n, code) :
    # 종료조건  
    if n > C-1 :
        if (len(code) == L) and (count_vowel(code)) >= 1 and (L-count_vowel(code) >= 2): 
            print(code)
        return
    
    # 하부함수
    dfs(n+1, code + candidate[n])
    dfs(n+1, code)

dfs(0, '')
