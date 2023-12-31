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
