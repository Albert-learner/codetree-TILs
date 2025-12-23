#include <iostream>
#include <vector>
using namespace std;

long long operate(int m, const vector<long long>& a_seq) 
{
    long long answer = 0;

    while (m >= 1) 
    {
        if (m % 2 == 1) 
        {
            answer += a_seq[m - 1];
            m -= 1;
        } 
        else 
        {
            answer += a_seq[m - 1];
            m /= 2;
        }
    }

    return answer;
}

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<long long> a_seq(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> a_seq[i];
    }

    cout << operate(M, a_seq);
    return 0;
}
