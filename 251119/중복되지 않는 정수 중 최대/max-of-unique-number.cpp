#include <iostream>
#include <vector>
#include <unordered_map>
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

    unordered_map<int, int> n_dict;
    n_dict.reserve(N);  

    for (int n : n_lst) 
    {
        n_dict[n]++;
    }

    int answer = -1;
    for (const auto &p : n_dict) 
    {
        int n = p.first;
        int cnts = p.second;
        if (cnts == 1) 
        {
            if (answer == -1 || n > answer) 
            {
                answer = n;
            }
        }
    }

    cout << answer << '\n';
    return 0;
}
