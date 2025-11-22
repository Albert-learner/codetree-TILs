#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M, 0));

    int num = 1;
    int ij_sum = 0;

    // Python의 while ij_sum <= N * M 에 맞춰 작성 (모든 칸 채워질 때까지 ij_sum 증가)
    while (ij_sum <= N * M) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (i + j == ij_sum) {
                    board[i][j] = num;
                    num++;
                }
            }
        }
        ij_sum++;
        if (num > N * M) break;   // 모든 숫자가 채워지면 종료 (python 코드에도 해당되는 종료 조건)
    }

    // 출력 (print(*row)와 동일하게 공백 구분)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << board[i][j];
            if (j + 1 < M) cout << " ";
        }
        cout << "\n";
    }

    return 0;
}
