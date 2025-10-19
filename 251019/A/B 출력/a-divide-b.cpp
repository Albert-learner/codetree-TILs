#include <iostream>
using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;

    // 정수 부분 출력
    cout << a / b << ".";

    a %= b;

    // 소수점 아래 20자리 계산
    for (int i = 0; i < 20; i++) {
        a *= 10;
        cout << a / b;
        a %= b;
    }

    cout << endl;
    return 0;
}
