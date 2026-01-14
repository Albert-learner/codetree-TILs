#include <iostream>
#include <vector>
using namespace std;


int main() 
{
    int n;
    cin >> n;

    // Please write your code here.
    vector<int>digits;

    while(true)
    {
        if(n < 2)
        {
            digits.push_back((int)n);
            break;
        }

        digits.push_back((int)(n % 2));
        n /= 2;
    }

    for(int i = (int)digits.size() - 1; i >= 0; i--)
        cout << digits[i];
    return 0;
}