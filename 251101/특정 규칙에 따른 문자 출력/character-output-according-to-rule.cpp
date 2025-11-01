#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    int rows = 2 * N - 1;
    vector<vector<char>> grid(rows, vector<char>(N, ' '));

    for (int i = 0; i < N; i++) {
        int x = rows - i;
        int y = i;
        for (int j = 0; j < N; j++) {
            int nx = x - 1;
            int ny = y;
            if (nx >= 0 && nx < rows && ny >= 0 && ny < N)
                grid[nx][ny] = '@';
            x = nx;
            y = ny;
        }
    }

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < N; j++) {
            cout << grid[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}
