#include <iostream>

#define MAX_N 10000

using namespace std;

int n;
int blocks[MAX_N];

int main() {
    // 입력:
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> blocks[i];
    
    // 전체 블럭 수를 셉니다.
    int sum_of_blocks = 0;
    for(int i = 0; i < n; i++)
        sum_of_blocks += blocks[i];
    
    // 평균 블럭 수 보다 더 큰 블럭에 대해서만
    // 그 차이만큼 옮겨주면 됩니다.
    int avg = sum_of_blocks / n;
    int ans = 0;
    for(int i = 0; i < n; i++)
        if(blocks[i] > avg)
            ans += blocks[i] - avg;

    cout << ans;
}
