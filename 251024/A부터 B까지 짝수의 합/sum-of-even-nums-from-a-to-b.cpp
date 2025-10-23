#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, evens_sum = 0;
    cin >> a >> b;

    for(int i = a; i <= b; i++)
    {
        if(i % 2 == 0)
            evens_sum += i;
    }
    cout << evens_sum;
    return 0;
}