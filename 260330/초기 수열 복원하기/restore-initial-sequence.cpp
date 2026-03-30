#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;

    vector<int> n_lst(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> n_lst[i];
    }

    for (int i = 0; i < N; i++) 
    {
        bool success = true;
        vector<int> originals(N, 0);
        originals[0] = i + 1;

        vector<bool> exist(N + 1, false);
        exist[originals[0]] = true;

        for (int j = 0; j < N - 1; j++) {
            int diff = n_lst[j] - originals[j];

            if (diff <= 0 || diff > N) {
                success = false;
                break;
            }

            if (exist[diff]) {
                success = false;
                break;
            }

            exist[diff] = true;
            originals[j + 1] = diff;
        }

        if (success) {
            for (int j = 0; j < N; j++) {
                cout << originals[j];
                if (j + 1 < N) cout << ' ';
            }
            cout << '\n';
            break;
        }

    }
    return 0;
}