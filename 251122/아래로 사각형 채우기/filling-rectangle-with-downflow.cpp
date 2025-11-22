#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    // N x N 보드 초기화
    vector<vector<int>> board(N, vector<int>(N, 0));

    int num = 0;
    // 바깥 루프: i = 열 인덱스
    // 안쪽 루프: j = 행 인덱스
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            num += 1;
            board[j][i] = num;   // Python의 board[j][i]와 동일
        }
    }

    // 출력 (print(*row)와 같은 형태)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j];
            if (j + 1 < N) cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
