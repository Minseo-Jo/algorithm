"""소수의 판별 알고리즘"""
# 2부터 자기자신-1까지 나누어보고 나누어떨어진다면 소수가 아님 -> O(N) 의 시간이 걸림
# 제곱근까지만 확인해줘도 됨
import math
n = int(input())
for i in range(2, int(math.sqrt(n)) + 1) :
    if n % i == 0 :
        print("not prime")
        exit()
print("prime")


"""에라토스테네스의 체 
1부터 N까지의 숫자 범위 중 모든 소수를 출력하는 알고리즘
1. 매 스텝마다 남은 수 중 가장 작은 i를 찾음 -> n의 제곱근까지만 탐색해주면 됨
2. i의 배수들은 모두 지워줌
3. 최종적으로 남은 숫자들이 소수
"""

import math
n = 1000 # 2부터 1000까지의 모든 수에 대한 소수 판별
array = [True for _ in range(n+1)] # 0과 1을 제외하고 모든 수는 일단 소수라고 초기화

for i in range(2, int(math.sqrt(n))+1) :
    if array[i] == True : # i가 소수라면
        #i의 배수들은 모두 삭제
        j = 2
        while i * j <= n :
            array[i*j] = False
            j += 1
for i in range(2, n+1) :
    if array[i] == True:
        print(i, end = ' ')
