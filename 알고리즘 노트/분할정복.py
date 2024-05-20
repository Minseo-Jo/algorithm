"""퀵소트
1. pivot은 array의 가장 첫번째 원소
2. left 는 pivot보다 큰 원소를 찾음
3. right 는 pivot보다 작은 원소를 찾음
4. 찾았으면 array[left], array[right] 교체
5. left와 right가 엇갈리면 array[pivot]과 array[right]교체
"""


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array) :
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))
