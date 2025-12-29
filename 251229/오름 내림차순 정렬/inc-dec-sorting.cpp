#include <iostream>
#include <vector>
#include <algorithm>
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

    sort(n_lst.begin(), n_lst.end());
    for (int i = 0; i < N; i++) 
    {
        cout << n_lst[i] << " ";
    }
    cout << '\n';

    for (int i = N - 1; i >= 0; i--) 
    {
        cout << n_lst[i] << " ";
    }

    return 0;
}
