#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, a, b, muls = 1;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> a >> b;
        for(int j = a; j <= b; j++)
        {
            muls *= j;
        }
        cout << muls << endl;
        muls = 1;
    }
    return 0;
}