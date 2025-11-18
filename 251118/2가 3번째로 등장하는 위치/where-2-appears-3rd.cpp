#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<int> n_lst(N);
    for (int i = 0; i < N; i++) {
        cin >> n_lst[i];
    }

    vector<int> twos;
    for (int i = 0; i < N; i++) 
    {
        if (n_lst[i] == 2) 
        {
            twos.push_back(i + 1); 
        }
    }

    cout << twos[2] << '\n'; 

    return 0;
}
