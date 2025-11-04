#include <iostream>
using namespace std;

int main()
 {
    // Please write your code here.
    int n, num = 0;
    cin >> n;

    for(int i = 1; i <= n * n; i++)
    {
        if(i % n == 0)
        {
            cout << i << ' ' << endl;
        }
        else
        {
            cout << i << ' ';
        }
    }
    return 0;
}