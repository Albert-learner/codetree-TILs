#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 0;

    while(cnts < 3)
    {
        cin >> n;

        if(n % 2 == 1)
            continue;
        else
        {
            cout << int(n / 2) << endl;
            cnts += 1;
        }
    }
    return 0;
}