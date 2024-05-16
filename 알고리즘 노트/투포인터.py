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
