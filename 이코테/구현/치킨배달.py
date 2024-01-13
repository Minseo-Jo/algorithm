import itertools


# 치킨집 좌표 구하기
def find_chicken(graph):
    chicken = []

    for i in range (N) : 
        for j, value in enumerate(graph[i]):
            if value == 2:
                x, y = i, j
                chicken.append((x,y))
    return chicken

# 집 좌표 구하기
def find_house(graph):
    house = []

    for i in range(N):
        for j, value in enumerate(graph[i]):
            if value == 1:
                x,y = i,j
                house.append((x,y))

    return house

N, M = map(int,input().split())

graph = []
for i in range (N) :
    graph.append(list(map(int, input().split())))


chicken_loc = find_chicken(graph)
house_loc = find_house(graph)

# 치킨집 조합 구하기
chicken_comb = []

for i in itertools.combinations(chicken_loc,M):
    chicken_comb.append(list(i))

# 거리 구하기
total_lst = []
for i in range (len(chicken_comb)):
    total_dist = 0
    for house in house_loc:
        min_dist = 100 
        for j in chicken_comb[i] :
            dist = abs(house[0] - j[0]) + abs(house[1] - j[1])
            if dist < min_dist :
                min_dist = dist
        total_dist += min_dist
    total_lst.append(total_dist)

print(min(total_lst))
