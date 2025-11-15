#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    long long N;
    cin >> N;

    vector<long long> fives;
    if (N == 5 || N == 10) 
        fives.push_back(N);

    long long idx = 1;
    vector<long long> n_lst;
    n_lst.push_back(N);

    while (fives.size() != 2) 
    {
        idx++;
        long long val = N * idx;
        if (val % 5 == 0) 
            fives.push_back(val);
        n_lst.push_back(val);
    }

    for (size_t i = 0; i < n_lst.size(); i++) 
    {
        if (i > 0) cout << ' ';
        cout << n_lst[i];
    }
    cout << '\n';

    return 0;
}
