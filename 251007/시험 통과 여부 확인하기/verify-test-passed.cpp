#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, diff;
    cin >> N;

    if(N < 80)
    {
        diff = 80 - N;
        cout << diff << " more score";
    }
    else
        cout << "pass";
    return 0;
}