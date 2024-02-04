def solution(friends, gifts):
    N = len(friends) 

    #주고 받은 선물 maps 초기화
    maps = [[0] * N for _ in range(N)]

    for gift in gifts :
        name = gift.split(" ")
        a = friends.index(name[0]) # 준 사람
        b = friends.index(name[1]) # 받은 사람
        maps[a][b] += 1 # maps 행렬 생성
        
    # 선물 지수 정보 저장
    gift_nums= []
    
    # 선물지수계산
    for r in range (N) :
        give, recieve = 0,0
        for c in range(N) :
            give += maps[r][c]
            recieve += maps[c][r]
        temp = give - recieve
        gift_nums.append(temp)
    
    # 선물 받은 수 계산
    answer = [0] * N    
    for i in range (N) :
        for j in range (i+1, N) :
            # 선물을 주고 받은 기록이 없거나 주고 받은 횟수가 같을 때
            if (maps[i][j] == 0 and maps[j][i] == 0) or (maps[i][j] == maps[j][i]) : 
                # 선물지수 비교 # 
                if gift_nums[i] > gift_nums[j] :
                    answer[i] += 1
                elif gift_nums[i] < gift_nums[j] :
                    answer[j] += 1
                else : # 선물지수가 같다면
                    continue
            else : # 선물 주고 받은 기록이 있다면
                # 준 횟수가 더 많은 사람이 선물 받기
                if maps[i][j] > maps[j][i] :
                    answer[i] += 1
                else : 
                    answer[j] += 1
                    
    ans = max(answer)
    return ans
