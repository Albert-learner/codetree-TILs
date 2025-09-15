#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;

    vector<int> total_n;
    for(int i = 1; i <= N * (N + 1) / 2; i++)
    {
        total_n.push_back(i);
    }

    int idx = 0;
    for(int i = 1; i <= N; i++)
    {
        for(int j = 0; j < i; j++)
        {
            cout << total_n[idx + j];
            if(j != i - 1)
                cout << ' ';
        }
        cout << endl;
        idx += i;
    }
    return 0;
}