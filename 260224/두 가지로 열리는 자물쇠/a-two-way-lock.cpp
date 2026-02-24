#include <bits/stdc++.h>
using namespace std;

static inline bool inRangeWrap(int center, int x, int N) 
{
    int d = abs(center - x);

    return (d <= 2) || (d >= N - 2);
}

int main() 
{
    int N;
    cin >> N;

    int a1, b1, c1, a2, b2, c2;
    cin >> a1 >> b1 >> c1;
    cin >> a2 >> b2 >> c2;

    long long cnts = 0, overlaps = 0;

    for (int i = 1; i <= N; i++) 
    {
        for (int j = 1; j <= N; j++) 
        {
            for (int k = 1; k <= N; k++) 
            {
                if (inRangeWrap(a1, i, N) && inRangeWrap(b1, j, N) && inRangeWrap(c1, k, N))
                    cnts++;

                if (inRangeWrap(a2, i, N) && inRangeWrap(b2, j, N) && inRangeWrap(c2, k, N))
                    cnts++;
            }
        }
    }

    for (int i = 1; i <= N; i++) 
    {
        for (int j = 1; j <= N; j++) 
        {
            for (int k = 1; k <= N; k++) 
            {
                if (inRangeWrap(a1, i, N) && inRangeWrap(b1, j, N) && inRangeWrap(c1, k, N) &&
                    inRangeWrap(a2, i, N) && inRangeWrap(b2, j, N) && inRangeWrap(c2, k, N))
                    overlaps++;
            }
        }
    }

    cout << (cnts - overlaps) << "\n";
    return 0;
}