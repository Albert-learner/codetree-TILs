#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    int N, n_new;
    cin >> N;

     int answer = 0, cnts = 0;
    long long num = 0; 
    for (int i = 0; i < N; i++) 
    {
        long long n_new;
        cin >> n_new;

        if (n_new > num) cnts += 1;
        else cnts = 1;

        answer = max(answer, cnts);
        num = n_new;
    }

    cout << answer << "\n";
    return 0;
}