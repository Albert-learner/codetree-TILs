#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<int>> grid(N);
    int cnts = 1;

    for (int i = 0; i < N; i++) 
    {
        if (i % 2 == 0) 
        {

            for (int j = 0; j < N; j++) 
            {
                grid[i].push_back(cnts + j);
            }
            cnts = grid[i].back() + 2;
        } 
        else 
        {
            for (int j = 0; j < N * 2; j += 2) 
            {
                grid[i].push_back(cnts + j);
            }
            cnts = grid[i].back() + 1;
        }
    }

    // 결과 출력
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            cout << grid[i][j];
            if (j != N - 1) cout << " ";
        }
        cout << "\n";
    }

    return 0;
}
