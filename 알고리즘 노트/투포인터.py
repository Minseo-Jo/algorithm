"""구간 합 구하기
1. 원하는 숫자 보다 크다면 start 인덱스를 이동
2. 원하는 숫자보다 작다면 end 인덱스를 이동
3. 원하는 숫자를 찾으면 정답 갱신 후 start 인덱스를 이동
"""

n, m = 5,5 # n : data 개수, m : 원하는 숫자
data = [1,2,3,2,5]

cnt = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n) :
    # end 를 가능한 만큼 이동시키기
    while interval_sum < m and end < n :
        interval_sum += data[end]
        end += 1
    if interval_sum == m :
        cnt += 1
    # 정답 갱신 후or 구간 합이 m보다 커지면 start 인덱스를 이동시켜야하니까 기존 구간 합에서 start값 빼주기
    interval_sum -= data[start]

print(cnt)


"""정렬되어있는 두 리스트(A, B)의 합 집합
1. i : A리스트 원소 가리키는 포인터, j : B리스트 원소 가리키는 포인터
2. A에서 처리되지 않은 원소 중 가장 작은 값을 i 가 가리킨다. 
3. B에서 처리되지 않은 원소 중 가장 작은 값을 j가 가리킨다.
4. A[i], B[j]중 작은 값을 결과 리스트에 담기
5. 작은 값을 가리켰던 포인터 이동
시간복잡도 O(N + M)
"""

n, m = 3, 4 # n : a 리스트 원소 개수, m : b 리스트 원소 개수
a = [1,3,5]
b= [2,4,6,8]

result = [0] * (n+m) # 결과 리스트
i,j,k = 0,0,0 # i : a 인덱스, j : b 인덱스, k : 결과리스트 인덱스

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m :
    # B의 리스트가 다 처리됐을때(남은 A 원소들 다 넣어주면됨) or 리스트 A의 원소가 더 작을 때(A의 원소를 넣어줘야함)
    if j >= m or (i < n and a[i] <= b[j]) :
        result[k] = a[i]
        i += 1
    else :
        result[k] = b[j]
        j += 1
    k += 1

print(*result)


"""슬라이딩 윈도우
 1. 멘 처음 범위의 수열의 합을 구한다.
 2. 맨 앞에 있는 리스트 값은 빼주고, 그 다음 리스트 값은 더해준다.
 => 계산의 중복 없이 값을 구할 수 있음 
 """
numbers = [1,3,2,6,-1,4,1,8,2]
n = len(numbers)
k = 5

window = sum(numbers[:k])
answer = window

for i in range (5, n) :
    window += numbers[i] - numbers[i-k]
    answer = max(answer, window)

print(answer)

