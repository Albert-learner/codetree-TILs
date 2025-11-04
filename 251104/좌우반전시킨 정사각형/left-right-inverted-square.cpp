#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    vector<vector<int>> square(n, vector<int>(n));
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= n; j++)
        {
            square[i - 1][j - 1] = i * j;
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = n - 1; j >=0; j--)
        {
            cout << square[i][j];
            if(j > 0) cout << " ";
        }
        cout << endl;
    }
    return 0;
}