#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<long long> a_seq(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> a_seq[i];
    }

    vector<long long> prefix(N + 1, 0);
    for (int i = 0; i < N; i++) 
    {
        prefix[i + 1] = prefix[i] + a_seq[i];
    }

    for (int i = 0; i < M; i++) 
    {
        int start, end;
        cin >> start >> end;
        cout << prefix[end] - prefix[start - 1] << '\n';
    }

    return 0;
}
