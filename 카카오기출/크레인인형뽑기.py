import numpy as np

def solution(board, moves):    
    basket = [] # out of range 에러 막기 위해 basket에 0 넣어주기
    cnt = 0

    # numpy array로 변환해서 전치행렬로 변환하기
    board = np.array(board)
    board = board.T

    #moves 도 numpy 변환해서 인덱스로 사용할 수 있도록
    moves = np.array(moves)
    moves = moves -1

    for i in moves:
        for j in range(len(board[0])):
            # board에 인형이 없다면 pass
            if board[i][j] == 0 :
                continue
            else : #인형이 있다면 basket에 넣어주고 0으로 바꿔줘야함
                basket.append(board[i][j])
                board[i][j] = 0
                break # 더이상 캐릭터 접근에 대한 루프(j) 돌면 안됨
    
        # moves 루프(i) 돌다가 같은 캐릭터 만나면 두개 모두 pop
        if (len(basket) >=2 ) and (basket[-1] == basket[-2]) : # out of range 에러 주의
            basket.pop()
            basket.pop()
            # pop 된 개수 세주기
            cnt += 2 
        else : 
            continue
    return cnt