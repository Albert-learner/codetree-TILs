#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N, K;
    cin >> N >> K;

    const int MAX_POS = 10000;
    vector<int> line(MAX_POS + 1, 0);

    for (int i = 0; i < N; i++) 
    {
        int pos;
        char alpha;
        cin >> pos >> alpha;
        line[pos] = (alpha == 'G') ? 1 : 2;
    }

    int windowSize = K + 1;

    long long windowSum = 0;
    for (int i = 0; i < windowSize; i++) windowSum += line[i];

    long long maxSum = windowSum;

    for (int i = windowSize; i <= MAX_POS; i++) 
    {
        windowSum += line[i];
        windowSum -= line[i - windowSize];
        maxSum = max(maxSum, windowSum);
    }

    cout << maxSum << "\n";
    return 0;
}