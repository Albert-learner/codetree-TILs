#include <iostream>
#include <vector>
using namespace std;

vector<int> seq;
int find_max(int n);

int main() 
{
    int N;
    cin >> N;

    seq.resize(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> seq[i];
    }

    cout << find_max(N - 1);
    return 0;
}

int find_max(int n) 
{
    if (n == 0) 
    {
        return seq[0];
    }
    return max(seq[n], find_max(n - 1));
}