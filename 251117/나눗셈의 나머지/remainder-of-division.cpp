#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int A, B, ans = 0;
    cin >> A >> B;

    int base = B;
    vector<int> rests(B, 0);
    while(A > 1)
    {
        int r = A % base;
        rests[r] += 1;
        A = A / base;
    }

    for(int i = 0; i < (int)rests.size(); i++)
    {
        ans += rests[i] * rests[i];
    }
    cout << ans;
    return 0;
}