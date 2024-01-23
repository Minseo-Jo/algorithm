sound = list(input())
duck = 0

# q로 시작, k로 마무리, 길이가 5로 나누어떨어지지 않는다면 녹음이 올바르지 않은 경우
if sound[0] != 'q' or sound[-1] != 'k' or len(sound) % 5 :
    print(-1)
    exit()


def find_duck(start) :
    quack = 'quack'
    j = 0 # quack 인덱스
    global duck
    new_duck = True # 새로운 오리를 구별하기 위한 flag

    for i in range (start, len(sound)) :
        if sound[i] == quack[j] :
            if sound[i] == 'k' :
                if new_duck : # 새로운 오리라면 개수 증가시켜주기
                    duck += 1
                    new_duck = False # 이제부터 나오는 오리는 기존의 오리
                j = 0 #다시 q부터 순회하면서 문자열 지워주기
                sound[i] = 0
                continue
            j += 1
            sound[i] = 0 # 오리 개수에 포함되는 문자열은 지워주기
                            

# q가 시작되는 인덱스부터 오리 개수 세기 시작
for i in range(len(sound)):
    if sound[i] == 'q' :
        find_duck(i)


# 모든 문자열이 지워져있지 않다면 잘못된 녹음
if any(sound) or duck == 0 :
    print(-1)
else:
    print(duck)
