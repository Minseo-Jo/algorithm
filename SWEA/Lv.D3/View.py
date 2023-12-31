T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    result = 0 
    for i in range (len(height)-4):
        semi_height = height[i:i+5]
        building = semi_height[2] # 가운데 빌딩 높이를 기준으로 해서 비교
        semi_height.sort()
        if (max(semi_height) == building): # 가운데 빌딩이 가장 높다면
            result += (building - semi_height[3]) # 두 번째로 높은 빌딩과의 차이가 조망권이 확보된 세대의 수
    print("#{0} {1}".format(test_case,result))
