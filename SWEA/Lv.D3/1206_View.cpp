#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	T = 10;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int N;
        int height[1000];
        int result = 0;
        //입력
        cin >> N;
        for (int i=0; i<N; ++i){
            cin >> height[i];
        }
        //각 빌딩마다 탐색
        for (int i = 0; i < N-4 ; ++i){
            vector<int>semi_height(height+i, height+i+5);
            int building = semi_height[2];
            sort(semi_height.begin(), semi_height.end());
            if (semi_height[4] == building){
                result += (building - semi_height[3]);
        	}
        }
       cout << "#" << test_case << " "<< result << endl;
    }
    return 0;
}



//2. 코드 최적화 풀이

#include <cstdio>
 
int max_v(int a, int b) { return a>b?a:b;}
 
int gm(int left, int right, int building_index, int height[], int &N){
    int maximum = 0;
    for (int i = left; i < right; i++){
        if (i == building_index) continue;
        maximum = max_v(maximum, height[i]); }
    return maximum; }
     
    int main (){
        int T = 10, test_case = 1, answer, N, maximum_height;
        int height[1000];
         
        while (T--){
            answer = 0 ; 
            //입력
            scanf("%d", &N);
            for (int i=0; i<N; i++){
                scanf("%d", &height[i]);}
             
            //빌딩 순회
            for (int i=2;i<N-2;i++){
                maximum_height = gm(i-2, (i + 3 < N) ? i + 3 : N, i, height, N); // i+3 이 N을 넘어가지 않도록 처리
                if (maximum_height < height[i])
                    answer += height[i] - maximum_height;
                }
            printf("#%d %d\n",  test_case++,  answer);
        }
        return 0;
    }
