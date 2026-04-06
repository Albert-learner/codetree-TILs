#include <iostream>

#define MAX_N 100

using namespace std;

int n;

int a[MAX_N], b[MAX_N];
int ans;

int main() {
    // 입력
    cin >> n;
    for(int i = 0 ; i < n; i++)
        cin >> a[i];
    for(int i = 0; i < n; i++)
        cin >> b[i];
  
    // 입력으로 주어진 사람 수를 보고
    // 최소 어느 만큼의 거리를 달려야 하는지 확인합니다.
    for(int i = 0; i < n; i++) {
        if(a[i] > b[i]) {
            // 최소 a[i] - b[i]명의 사람들은 오른쪽으로 달려야 합니다.
            int num = a[i] - b[i];
            a[i] -= num;
            a[i + 1] += num;
            ans += num;
        }
    }

    cout << ans;

    return 0;
}
