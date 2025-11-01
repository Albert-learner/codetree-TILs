#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    int size = 2 * N - 1;
    vector<vector<char>> pattern(size, vector<char>(size, ' '));

    for (int i = 0; i < N; i++) {
        for (int j = i; j < size - i; j++) {
            pattern[i][j] = '*';
            pattern[size - i - 1][j] = '*';
        }
    }

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cout << pattern[i][j];
            if (j < size - 1) cout << ' ';  // 공백 추가
        }
        cout << endl;
    }

    return 0;
}
