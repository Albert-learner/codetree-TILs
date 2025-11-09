#include <bits/stdc++.h>
using namespace std;

int main() {
    long long start, end;
    if (!(cin >> start >> end)) return 0;

    int complete_nums = 0;
    for (long long N = start; N <= end; ++N) 
    {
        long long sum_div = 0; 
        for (long long i = 1; i * i <= N; ++i) 
        {
            if (N % i == 0) 
            {
                long long j = N / i;
                sum_div += i;
                if (j != i) sum_div += j; 
            }
        }
        sum_div -= N; 

        if (sum_div == N) ++complete_nums; 
    }

    cout << complete_nums << '\n';
    return 0;
}
