#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<long long>> triangle;

    for (int i = 0; i < N; i++) 
    {
        vector<long long> row(i + 1, 1);

        for (int j = 1; j < i; j++) 
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];

        triangle.push_back(row);
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < (int)triangle[i].size(); j++) 
        {
            cout << triangle[i][j];
            if (j + 1 < (int)triangle[i].size()) cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
