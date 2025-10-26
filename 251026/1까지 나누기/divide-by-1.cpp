#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, i = 1, cnts = 0;
    cin >> n;

    while(i >= 1)
    {
        n /= i;
        if(n <= 1)
        {
            cnts += 1;
            break;
        }
        i += 1;
        cnts += 1;
    }
    cout << cnts;
    return 0;
}