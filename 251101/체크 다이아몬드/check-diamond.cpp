#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    // 위쪽 삼각형
    for (int i = 0; i < N; i++) {
        for (int j = N; j > i + 1; j--) {
            cout << ' ';
        }
        for (int j = 0; j < i + 1; j++) {
            cout << "* ";
        }
        cout << endl;
    }

    // 아래쪽 삼각형
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < i; j++) {
            cout << ' ';
        }
        for (int j = N; j > i; j--) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
