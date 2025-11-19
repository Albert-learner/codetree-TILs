#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, last_idx = 0;
int a[1000];

int main() 
{
    cin >> N;

    for (int i = 0; i < N; i++) 
    {
        cin >> a[i];
    }

    // Please write your code here.
    vector<int> indices;
    indices.push_back(0);

    for(int i = 1; i < N; i++)
    {
        last_idx = indices[indices.size() - 1];
        if(a[i] > a[last_idx])
            indices.push_back(i);
    }

    reverse(indices.begin(), indices.end());
    for(int idx: indices)
        cout << idx + 1 << ' ';
    return 0;
}
