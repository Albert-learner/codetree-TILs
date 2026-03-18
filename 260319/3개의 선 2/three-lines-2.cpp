#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<int> x, y;
    vector<vector<int>> xy(11, vector<int>(11, 0));
    vector<string> cases = {"xxx", "xxy", "xyx", "yxx", "yyy", "yyx", "yxy", "xyy"};

    // Please write your code here.
    for (int t = 0; t < N; t++) 
    {
        int xi, yi;
        cin >> xi >> yi;
        x.push_back(xi);
        y.push_back(yi);
        xy[xi][yi] = 1;
    }

    auto go = [&](int n, char chr) -> int 
    {
        int sum_ = 0;
        if (chr == 'x') 
        {
            for (int i = 0; i < 11; i++) 
            {
                sum_ += xy[i][n];
            }
        } 
        else 
        {
            for (int i = 0; i < 11; i++) 
            {
                sum_ += xy[n][i];
            }
        }
        return sum_;
    };

    for (const string& cse : cases) 
    {
        char c1 = cse[0], c2 = cse[1], c3 = cse[2];

        for (int i = 0; i < 6; i++) 
        {
            for (int j = 0; j < 6; j++) 
            {
                for (int k = 0; k < 6; k++) 
                {
                    if (i == j || j == k || k == i) 
                    {
                        continue;
                    }

                    int sum_ = 0;
                    sum_ += go(i, c1);
                    sum_ += go(j, c2);
                    sum_ += go(k, c3);

                    if (sum_ == N) 
                    {
                        cout << 1 << '\n';
                        return 0;
                    }
                }
            }
        }
    }

    cout << 0 << '\n';
    return 0;
}