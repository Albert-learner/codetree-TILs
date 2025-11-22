#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M));
    int num = 0;

    for (int j = 0; j < M; j++) {
        if (j % 2 == 0) {              // 짝수 번째 열 → 위에서 아래로
            for (int i = 0; i < N; i++) {
                board[i][j] = num;
                num++;
            }
        } else {                       // 홀수 번째 열 → 아래에서 위로
            for (int i = N - 1; i >= 0; i--) {
                board[i][j] = num;
                num++;
            }
        }
    }

    // 출력 (print(*row) 동일)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << board[i][j];
            if (j + 1 < M) cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
