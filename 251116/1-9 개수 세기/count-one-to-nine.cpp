#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<int> n_lst(N);
    for (int i = 0; i < N; i++) 
        cin >> n_lst[i];

    vector<int> n_lst_cntr(10, 0);

    for (int n : n_lst) 
    {
        if (1 <= n && n <= 9)
            n_lst_cntr[n]++;        
    }

    for (int i = 1; i <= 9; i++)
        cout << n_lst_cntr[i] << '\n';

    return 0;
}
