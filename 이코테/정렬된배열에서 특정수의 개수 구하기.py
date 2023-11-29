#조건 : 시간복잡도 O(logn)
# 처음으로 원하는 숫자가 나온 인덱스와 마지막으로 나온 인덱스 차이를 구하는 것이 핵심

def solution(array, x):
    n = len(array)

    # 첫번째 인덱스 확인
    a = first(array, x, 0, n-1)

    #마지막 인덱스 확인
    b = last(array,x, 0, n-1)

    return b - a + 1 #개수니까 +1






# 처음 원하는 숫자가 나온 인덱스를 찾는 함수 
def first(array, target, start, end):
    while (start <= end) :
        mid = (start+end) //2

        if array[mid] == target:
            return mid
        # 찾고자하는 값이 왼쪽에 있는 경우만 인덱스 반환
        elif target > array[mid-1]:
            return mid
        # 중간값보다 찾는 값이 작으면 왼쪽 
        elif array[mid] >= target:
            return first(array, target, start, mid-1)
        else:
            # 중간값보다 크다면 오른쪽 확인
            return first(array, target, mid+1, end)
        

# 원하는 숫자가 나오는 마지막 위치를 찾는 함수
def last(array, target ,start, end):
    while(start<=end ):
        mid = (start + end) //2

        if array[mid] == target:
            return mid
        # 찾고자하는 값이 가장 오른쪽에 있는 경우만 인덱스 반환
        elif target < array[mid+1]:
            return mid
        # 찾고자하는 값이 중간값보다 작다면 왼쪽 확인
        elif array[mid] > target :
            return last(array, target, start, mid-1)
        else:
            # 중간값보다 크다면 오른쪽 확인
            return last(array, target, mid+1, end)


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = solution(array,x)

print(count)

